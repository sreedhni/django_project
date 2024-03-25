from django.urls import path
from users.views import *

urlpatterns=[
    path('register-applicant/',register_applicant,name="register-applicant"),
    path('register-recruiter/',register_recruiter,name="register-recruiter"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout"),
    path('<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),



]