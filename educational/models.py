from django.db import models

# Create your models here.

class BlogPosts (models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    cover = models.ImageField(upload_to="", blank=True, verbose_name="پوستر مقاله")
    description = models.TextField(verbose_name="توضیحات مقاله")
    


class LearningVideos (models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان ویدیو")
    video = models.FileField(upload_to="ویدیو")

