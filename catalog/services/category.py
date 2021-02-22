from catalog.models import Category

class CagegoryService:
    """ Services for categories """
    @staticmethod
    def get_data(slug):
        return {
                "category": Category.objects.get(is_active=True, slug=slug)
        }
