from catalog.models import Category, Item, Characteristic
from django.db.models.query import QuerySet

def get_active_categories() -> QuerySet:
    """ Get all active categories """
    return Category.objects.filter(is_active=True)

def get_active_category_data(slug) -> dict:
    """ Get all data of active category with slug that we give """
    category = get_active_category_by_slug(slug)
    items = get_active_items_by_category_id(category.id)
    filters = get_filter_by_category_id(category.id)
    return {
            "category": category,
            "items": items,
            "filters": filters
    }

def get_active_category_by_slug(slug) -> QuerySet:
    """ Get categry that active and has slug that we give """
    return Category.objects.get(is_active=True, slug=slug)

def get_active_items_by_category_id(category_id) -> QuerySet:
    """ Get items that active and have category_id that we give """
    return Item.objects.filter(is_active=True, category_id=category_id)

def get_filter_by_category_id(category_id) -> QuerySet:
    """ Get list of filters(characteristics) for category """
    return Characteristic.objects.filter(is_active=True, category_id=category_id)
