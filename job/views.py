from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from.models import Job,ApplyJob
from job.forms import *
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import ApplyJob
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Notification


def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var= form.save(commit=False)
                var.user= request.user
                var.company= request.user.company
                var.save()
                messages.info (request, 'New job has been created')
                return redirect('manage-jobs')

            else:
                messages.warning (request, 'Something went wrong')
                return redirect("create-job")
        else:
            form = CreateJobForm()
            context = {'form':form}
            return render(request, 'job/create_job.html',context)
    else:
        messages.warning (request, 'permission denied')
        return redirect("dashboard")
    
def update_job(request, pk):
    job_instance = Job.objects.get(pk=pk)  

    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job_instance)
        if form.is_valid():
            form.save()
            messages.info(request, 'Job has been updated successfully.')
            return redirect('manage-jobs')
        else:
            messages.warning(request, 'Something went wrong. Please check the form.')
    else:
        form = UpdateJobForm(instance=job_instance)
    
    context = {'form': form}
    return render(request, 'job/update_job.html', context)  


def manage_jobs(request):
    jobs=Job.objects.filter(user=request.user,company=request.user.company)
    context={"jobs":jobs}
    return render(request, 'job/manage_job.html',context)



def send_notification_email(notification):
    subject = 'New Job Application Notification'
    html_message = render_to_string('job/notification_email.html', {'notification': notification})
    plain_message = strip_tags(html_message)
    from_email = "admin@gmail.com"  
    to_email = notification.receiver.user.email
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

def apply_to_job(request, pk): 
    try:
        job = Job.objects.get(pk=pk)
        existing_application = ApplyJob.objects.filter(user=request.user, job=job).exists()
        if not existing_application:
            notification_message = (
                f"Hello, {job.company}\n\n"
                f"A new job application has been received for the position \"{job.title}\".\n\n"
                f"Please login to your dashboard to view the details.\n\n"
                "Thank you!"
            )
            notification = Notification.objects.create(
                sender=request.user,
                receiver=job.company,
                message=notification_message
            )
            apply_job = ApplyJob.objects.create(user=request.user, job=job)
            send_notification_email(notification)
            
            applicant_subject = 'Application Confirmation'
            applicant_message = f"Hello, {request.user}!\n\nYou have submitted an application for the position: {job.title}."
            "Thank you!"
            send_mail(applicant_subject, applicant_message, "admin@gmail.com", [request.user.email])
            
            return redirect('applied-jobs')
        else:
            messages.warning(request, 'You have already applied to this job.')
            return redirect('applied-jobs')
    except Job.DoesNotExist:
        return HttpResponseNotFound('<h1>Job not found</h1>')

def all_applicants(request, pk):
    try:
        job = Job.objects.get(pk=pk)
        applicants = job.applyjob_set.all()
        context = {'job': job, 'applicants': applicants}
        return render(request, 'job/all_applicants.html', context)
    except Job.DoesNotExist:
        return HttpResponseNotFound('<h1>Job not found</h1>')

def change_applicant_status(request, apply_job_id, new_status):
    try:
        apply_job = ApplyJob.objects.get(pk=apply_job_id)
        previous_status = apply_job.status
        apply_job.status = new_status
        apply_job.save()
        subject = f'Status Update: {apply_job.job.title}'
        recipient_email = apply_job.user.email

        if new_status == 'Accepted':
            message = f'Hello {apply_job.user.username},\n\nThe status of your job application for "{apply_job.job.title}" has been changed from "{previous_status}" to "{new_status}".\n\nCongratulations! You have been selected. Our recruiter will contact you soon.\n\nwith regards, \n\n {apply_job.job.company}'
        elif new_status == 'Declined':
            message = f'Hello {apply_job.user.username},\n\nThe status of your job application for "{apply_job.job.title}" has been changed from "{previous_status}" to "{new_status}".\n\nWe regret to inform you that your application has been declined. Unfortunately, we are moving forward with other candidates.\n\nwith regards, \n\n {apply_job.job.company}'
        else:
            message = f'Hello {apply_job.user.username},\n\nThe status of your job application for "{apply_job.job.title}" has been changed from "{previous_status}" to "{new_status}".'
        send_mail(subject, message, 'your_email@example.com', [recipient_email])

        return redirect('all-applicant', pk=apply_job.job.pk)
    except ApplyJob.DoesNotExist:
        return HttpResponseNotFound('<h1>Application not found</h1>')


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import ApplyJob


def applied_jobs(request):
    if request.user.is_authenticated and request.user.is_applicant:
        applied_jobs = ApplyJob.objects.filter(user=request.user, is_active=True)
        context = {'applied_jobs': applied_jobs}
        return render(request, 'job/applied_jobs.html', context)
    else:
        return render(request, 'job/unauthorized.html')
    
