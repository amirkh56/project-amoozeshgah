from django.contrib import admin
from .models import BlogPosts, LearningVideos

# Register your models here.

admin.site.register(BlogPosts)
admin.site.register(LearningVideos)