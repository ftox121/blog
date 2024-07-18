from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from blogapp.forms import RegisterForm, CreatePostForm
from django.contrib import messages

from blogapp.models import Posts


# Create your views here.

@login_required
def home(request):
    posts = Posts.objects.all()
    return render(request , 'blogapp/home.html', {'posts' : posts})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('blogapp:home   ')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('blogapp:home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def about_view(request):
    return render(request , 'blogapp/about.html')
@login_required
def profile(request):
    return render(request, 'blogapp/profile.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogapp:home')
    else:
        form = CreatePostForm()
    return render(request, 'blogapp/create_post.html', {"form" : form})

@login_required
def delete_view(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogapp:home')
    return render(request, 'blogapp/delete.html',{'post':post})