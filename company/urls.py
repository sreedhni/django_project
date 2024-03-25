from django.urls import path
from company.views import *

urlpatterns=[
    path('update-company/',update_company,name="update-company"),
    path('company-details/<int:pk>/',company_details,name="company-detail"),
    path('company-delete/<int:pk>/',companyDeleteView.as_view(),name="company-delete"),





]