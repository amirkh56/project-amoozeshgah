from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin (UserAdmin):
    list_display = ['username', 'email', 'age', 'is_superuser']

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
        (None, {
            'fields': (
                ('age',)
            ),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)