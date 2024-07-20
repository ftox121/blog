from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Posts.Status.PUBLISHED)




class Posts(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=32)
    content = models.TextField(max_length=264)
    slug = models.SlugField(max_length=250, default=True, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE, null=True, related_name='blog_posts')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    object = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:post_detail', args=[self.publish.year, self.publish.month, self.publish.day,self.slug])