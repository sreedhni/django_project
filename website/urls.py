from django.urls import path
from website.views import *

urlpatterns=[
    path('',home,name="home"),
    path('job-listing/',job_listing,name="job-listing"),
    path('job-details/<int:pk>/',job_details,name="job-details"),
    path('search/',SearchView.as_view(),name="search")




]