from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import regform
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = regform
    form = regform
    model = CustomUser
    list_display = ['username', 'year']


admin.site.register(CustomUser, CustomUserAdmin)
