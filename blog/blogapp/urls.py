from django.urls import path

from blogapp.views import home, register, login_view, about_view, profile, create_post, delete_view, post_detail, \
    post_share

app_name = 'blogapp'

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('about/', about_view, name='about'),
    path('profile/', profile, name='profile'),
    path('create/', create_post, name='create'),
    path('delete/<int:pk>', delete_view, name="delete_post"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_pk>/', post_share, name='post_share'),
]