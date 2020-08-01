from django import forms
from django.forms import ModelForm
from first_app.models import *


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(widget = forms.PasswordInput())


class CreatePollForm(forms.Form):
    name = forms.CharField(max_length = 100)
    description = forms.CharField(max_length = 100)


class LoginForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


