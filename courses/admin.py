from django.contrib import admin
from .models import LearningCourses, LearningWorkshops

# Register your models here.

admin.site.register(LearningCourses)
admin.site.register(LearningWorkshops)