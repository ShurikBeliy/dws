from django.contrib import admin
from .models import *
from .admin_mixin import *

@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name', 'category', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'category', 'priority',)
    search_fields = ('name',)

class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    fields = ('is_active','name','priority')
    classes = ('collapse',)
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'slug', 'name', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'priority',)
    search_fields = ('name','slug',)
    inlines=(CharacteristicInline,)

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    fields = ('is_active','alt','image','priority')
    classes = ('collapse',)
    extra = 0

class CharacteristicValueInline(admin.TabularInline):
    model = CharacteristicValue
    fields = ('is_active','characteristic',)
    classes = ('collapse',)
    extra = 0

@admin.register(Item)
class ItemAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ('is_active', 'category_column', 'slug', 'name', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'priority',)
    search_fields = ('name','slug',)
    inlines=(CharacteristicValueInline, ItemImageInline)
