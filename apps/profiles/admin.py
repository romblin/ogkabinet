from django.contrib import admin

from .models import UserProfile


class UserProfileTabular(admin.TabularInline):
    model = UserProfile
