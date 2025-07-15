from django.shortcuts import render
from django.views import generic
from .models import Schedule
from courses.models import LearningCourses


class CalenderView (generic.TemplateView) :
    template_name = 'homeapp/learningcalender.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = LearningCourses.objects.all()
        context['schedule'] = Schedule.objects.all()
        return context