from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from blogapp.forms import RegisterForm, CreatePostForm
from django.contrib import messages
from django.http import Http404
from blogapp.models import Posts
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from blogapp.forms import  EmailPostForm
from django.core.mail import send_mail
# Create your views here.

@login_required
def home(request):
    post_list = Posts.published.all()
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request , 'blogapp/home.html', {'posts' : posts})



def post_detail(request,year, month, day, post):
    post = get_object_or_404(Posts, status=Posts.Status.PUBLISHED, slug=post,publish__year=year,publish__month=month,publish__day=day)
    return render(request, 'blogapp/detail.html', {'post' : post})

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


def post_share(request , post_pk):
    post = get_object_or_404(Posts, pk=post_pk,status=Posts.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} reccomends you read " f"{post.title}"
            message = f'Read {post.title} at {post_url}\n\n' f'{cd['name']} comments: {cd['comments']}'
            send_mail(subject,message,'lstaeee111@gmail.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blogapp/share.html', {'form':form, 'post': post, 'sent': sent})

