from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User
from .form import RegisterUserForm
from resume.models import*
from company.models import *
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import  get_user_model

def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = True
            user.username = user.email
            user.save()
            Resume.objects.create(user=user)
            messages.info(request, 'Your account has been created.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_applicant.html', context)
    
def register_recruiter(request):
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_recruiter=True
            var.username=var.email
            var.save()
            Company.objects.create(user=var)
            messages.info (request, 'Your account has been created.')
            return redirect('login')
        else:
            messages.warning (request, 'Something went wrong')
            return redirect('register-recruiter')

    else:

        form = RegisterUserForm()

        context = {'form':form}

        return render(request, 'users/register_recruiter.html',context)
    
# login a user
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate (request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.warning (request, 'Something went wrong')
            return redirect('login')
    else:
        return render (request, 'users/login.html')
def logout_user(request):
    logout(request)
    messages.info(request,"your session expired")
    return redirect("home")


@method_decorator(login_required, name='dispatch')
class ProfileDeleteView(DeleteView):
    template_name = 'users/profile_delete.html'
    model = get_user_model()
    success_url = reverse_lazy('dashboard')
