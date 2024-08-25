# This is accounts/admin.py documentation

from django.contrib import admin
from .models import UserProfile

# Register your models here.

admin.site.register(UserProfile)