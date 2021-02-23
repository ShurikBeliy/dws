from django.shortcuts import render
from core.views import BaseView
from .services.category import get_category_active_data

class CategoryDetail(BaseView):
    """ View for category page """
    def get(self, request, slug):
        return render(request, 'catalog/category.html',
                      get_category_active_data(slug))
