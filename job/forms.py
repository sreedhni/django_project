from django import forms
from .models import*

class CreateJobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=("user",'company','cover_letter')

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=("user",'company','cover_letter','status')
