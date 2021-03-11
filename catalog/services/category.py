from catalog.models import Category, Item

def get_active_categories():
    """ Get all active categories """
    return Category.objects.filter(is_active=True)

def get_active_category_data(slug):
    """ Get all data of active category with slug that we give """
    category = get_active_category_by_slug(slug)
    items = get_active_items_by_category_id(category.id)
    return {
            "category": category,
            "items": items
    }

def get_active_category_by_slug(slug):
    """ Get categry that active and has slug that we give """
    return Category.objects.get(is_active=True, slug=slug)

def get_active_items_by_category_id(category_id):
    """ Get items that active and have category_id that we give """
    return Item.objects.filter(is_active=True, category_id=category_id)
