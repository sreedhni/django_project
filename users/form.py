
from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    usertype = forms.ChoiceField(choices=[('jobseeker', 'Jobseeker'), ('recruiter', 'Recruiter')])

    class Meta:
        model = get_user_model()
        fields = ["email", 'password1', 'password2', 'usertype']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")
        if password1.isdigit():
            raise ValidationError("Your password can't be entirely numeric.")
        return password1
