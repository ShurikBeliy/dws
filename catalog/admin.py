from django.contrib import admin
from django.urls import resolve
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
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(CharacteristicValueInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        # We need to change queryset for characteristic field because we don't want to show characteristics from other categories
        if db_field.name == 'characteristic':
            resolved = resolve(request.path_info)
            try: # we can have exceptions for new items
                item = Item.objects.get(pk=resolved.kwargs['object_id'])
                field.queryset = item.category.characteristics.filter(is_active=True)
            except:
                pass
        return field

@admin.register(Item)
class ItemAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ('is_active', 'category_column', 'slug', 'name', 'priority',)
    list_display_links = ('name',)
    list_editable = ('is_active', 'priority',)
    search_fields = ('name','slug',)
    inlines=(CharacteristicValueInline, ItemImageInline)
