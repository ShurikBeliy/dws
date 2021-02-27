from django.contrib import admin
from .models import *
from .admin_mixin import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'slug', 'name', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'priority',)
    search_fields = ('name','slug',)

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    fields = ('is_active','alt','image','priority')
    classes = ('collapse',)
    extra = 0

@admin.register(Item)
class ItemAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ('is_active', 'category_column', 'slug', 'name', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'priority',)
    search_fields = ('name','slug',)
    inlines=(ItemImageInline,)
