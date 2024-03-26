from django.urls import path
from .views import *

urlpatterns=[
    path('create-job/',create_job,name="create-job"),
path('job/update-job/<int:pk>/', update_job, name='update-job'),

    path('manage-jobs/',manage_jobs,name="manage-jobs"),
    path('apply-to-job/<int:pk>/',apply_to_job,name="apply-to-job"),
    path('all-applicant/<int:pk>/',all_applicants,name="all-applicant"),
    path('change-status/<int:apply_job_id>/<str:new_status>/',change_applicant_status, name='change-status'),
path('applied-jobs/', applied_jobs, name='applied-jobs'),


]