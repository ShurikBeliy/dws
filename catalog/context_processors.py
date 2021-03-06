from .services.category import get_active_categories

def categories(request) -> dict:
    """ Get all active categories for context """
    categories = get_active_categories()
    return {'categories': categories}
