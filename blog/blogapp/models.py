from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Posts(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=32)
    content = models.TextField(max_length=264)
    slug = models.SlugField(max_length=250, default=True)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE, null=True, related_name='blog_posts')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

