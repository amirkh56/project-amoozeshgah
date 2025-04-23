from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import WinterSchedule, AutumnSchedule

# Register your models here.



    
admin.site.register(WinterSchedule)
admin.site.register(AutumnSchedule)
