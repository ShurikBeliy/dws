from django.shortcuts import render
from core.views import BaseView
from .services.category import get_active_category_data

class CategoryDetail(BaseView):
    """ View for category page """
    def get(self, request, slug):
        return render(request, 'catalog/category.html',
                      get_active_category_data(slug))
