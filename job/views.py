from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from.models import Job,ApplyJob
from job.forms import *
from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponseNotFound

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

def apply_to_job(request, pk): 
    if request.user.is_authenticated and request.user.is_applicant:
        job=Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user,job=pk).exists():
            messages.warning(request,"permission denied")
            return redirect("dashboard")
        else:
            ApplyJob.objects.create(job=job,user=request.user,status="pending")
            messages.info(request, "You have successfully applied! Please see dashboard")
            return redirect('applied-jobs')
    else:
        messages.info(request, "please login")
        return redirect('login')
def all_applicants(request, pk):
    try:
        job = Job.objects.get(pk=pk)
        applicants = job.applyjob_set.all()
        context = {'job': job, 'applicants': applicants}
        return render(request, 'job/all_applicants.html', context)
    except Job.DoesNotExist:
        return HttpResponseNotFound('<h1>Job not found</h1>')
    
from django.shortcuts import render
from .models import ApplyJob

def applied_jobs(request):
    if request.user.is_authenticated and request.user.is_applicant:
        applied_jobs = ApplyJob.objects.filter(user=request.user)
        context = {'applied_jobs': applied_jobs}
        return render(request, 'job/applied_jobs.html', context)
    else:
        return render(request, 'job/unauthorized.html')

from django.shortcuts import get_object_or_404, redirect
from .models import ApplyJob

def delete_applied_job(request, job_id):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_applicant:
            applied_job = get_object_or_404(ApplyJob, id=job_id, user=request.user)
            if applied_job:
                applied_job.delete()
                messages.success(request, "Applied job deleted successfully.")
            else:
                messages.error(request, "Failed to delete applied job.")
            return redirect('applied_jobs')
    return redirect('dashboard')  


def job_list(request):
    jobs = Job.objects.filter(is_available=True)  

    if request.method == 'GET':
        form = CreateJobForm(request.GET)
        if form.is_valid():
            keywords = form.cleaned_data.get('keywords')
            location = form.cleaned_data.get('location')
            min_salary = form.cleaned_data.get('min_salary')
            max_salary = form.cleaned_data.get('max_salary')

            if keywords:
                jobs = jobs.filter(
                    Q(title__icontains=keywords) |
                    Q(description__icontains=keywords) |
                    Q(requirements__icontains=keywords) |
                    Q(ideal_candidate__icontains=keywords)
                )

            if location:
                jobs = jobs.filter(location__icontains=location)

            if min_salary:
                jobs = jobs.filter(salary__gte=min_salary)

            if max_salary:
                jobs = jobs.filter(salary__lte=max_salary)

    else:
        form = CreateJobForm()

    context = {
        'jobs': jobs,
        'form': form,
    }
    return render(request, 'job/search.html', context)

