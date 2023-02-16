

from .models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control my-2","placeholder":"enter your name"}))
    email = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control my-2"}))
    password1 = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control my-2"}))
    password2 = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control my-2"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
