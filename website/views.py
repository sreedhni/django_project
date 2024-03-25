from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from job.models import Job,ApplyJob
def home (request):
    jobs=Job.objects.filter(is_available=True).order_by('timestamb')

    context = {'jobs':jobs}

    return render (request, 'website/home.html',context)
    

def job_listing (request):
    jobs=Job.objects.filter(is_available=True).order_by('timestamb')
    context = {'jobs':jobs}
    return render(request, 'website/job_listing.html',context)


from django.contrib import messages

@login_required
def job_details(request, pk):
    try:
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            has_applied = True
        else:
            has_applied = False
        job = Job.objects.get(pk=pk)
        
        context = {
            'job': job,
            'has_applied': has_applied
        }
        return render(request, 'website/job_detail.html', context)
    except Job.DoesNotExist:
        messages.error(request, "Job not found.")
        return redirect('job_list')  
from django.http import Http404

from django.http import Http404

from django.views.generic import ListView

from django.shortcuts import render
from django.views.generic import ListView

from django.views.generic import ListView
class SearchView(ListView):
    model = Job
    template_name = 'website/search.html'
    context_object_name = 'jobapp'

    def get_queryset(self):
        queryset = super().get_queryset()    
        title = self.request.GET.get('job_title', '')
        location = self.request.GET.get('job_location', '')
        employment_type = self.request.GET.get('employment_type', '')
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if employment_type:
            queryset = queryset.filter(Employment_Type__icontains=employment_type)
    
        return queryset

