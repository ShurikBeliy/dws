from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'slug', 'name', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'priority',)
    search_fields = ('name','slug',)
