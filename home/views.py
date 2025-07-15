from django.shortcuts import render
from django.views import generic
from courses.models import LearningCourses

# Create your views here.


class HomeView (generic.TemplateView) :
    template_name = "homeapp/home.html"
    context_object_name = 'LearningCourses'