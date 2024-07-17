from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=264)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

