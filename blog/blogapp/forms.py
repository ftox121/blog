from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from blogapp.models import Posts


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content','image']