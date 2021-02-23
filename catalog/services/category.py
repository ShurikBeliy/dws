from catalog.models import Category, Item

def get_category_active_data(slug):
    """ Get all data of category with slug that we give """
    category = get_active_categry_by_slug(slug)
    return {
            "category": category,
            "items": get_categry_active_items(category.id)
    }

def get_active_categry_by_slug(slug):
    """ Get categry that active and has slug that we give """
    return Category.objects.get(is_active=True, slug=slug)

def get_categry_active_items(category_id):
    """ Get items that active and have category_id that we give """
    try:
        return Item.objects.filter(is_active=True, category_id=category_id)
    except Exception as e:
        return None
