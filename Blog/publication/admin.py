from django.contrib import admin
from .models import *


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_time', 'slug')
