from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q
from django.http import HttpRequest

UserModel=get_user_model()
class EmailBackend(ModelBackend):
    def authenticate(self, request,username=None,password=None, **kwargs) :
        try:
            user=UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return
        except UserModel.MultipleObjectsReturned:
            user=UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        if user.check_password(password) and self.user_can_authenticate(user):
            return user



        


        return super().authenticate(request, username, password, **kwargs)