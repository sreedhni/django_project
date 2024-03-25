from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .foms import * 
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from job.models import*

def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == 'POST':
            form=UpdateCompanyForm(request.POST, instance=company)
            if form.is_valid():
                var=form.save(commit=False)
                user= User.objects.get(id=request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.info (request, 'Your company is now active. You can start creating job ads')
                return redirect('dashboard')
            else:
                messages.warning (request, 'Something went wrong')
        else:
            form=UpdateCompanyForm(instance=company)
            context = {'form': form}
            return render(request, 'company/update_company.html',context)
    else:
        messages.danger(request, 'permission denaied')

        return redirect("dashboard")

#view company details

def company_details (request, pk):
    company=Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request, 'company/company_details.html',context)
class companyDeleteView(DeleteView):
    template_name = 'company/company_delete.html'
    model =Job
    success_url = reverse_lazy('dashboard')
