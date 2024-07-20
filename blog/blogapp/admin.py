from django.contrib import admin

from blogapp.models import Posts

# Register your models here.


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'slug', 'publish','status']
    list_filter = ['status', 'created_at', 'publish', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
