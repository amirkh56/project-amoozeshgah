from django.shortcuts import render
from django.views import generic
from .models import Schedule


class CalenderView (generic.TemplateView) :
    template_name = 'homeapp/learningcalender.html'
    model = Schedule
    context_object_name = 'Schedule'