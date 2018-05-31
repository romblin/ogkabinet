from django.contrib import admin

from kabinet.common.admin import site
from .models import KUser


@admin.register(KUser, site=site)
class KUserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'phone', 'is_active')
    search_fields = ('username', 'first_name', 'email', 'phone')
