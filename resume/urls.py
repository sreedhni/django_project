from django.urls import path
from resume.views import *

urlpatterns=[
    path('update-resume',update_resume,name="update-resume"),
    path('resume-detail/<int:pk>/',resume_details,name="resume-details"),




]