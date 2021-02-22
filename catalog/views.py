from django.shortcuts import render
from core.views import BaseView
from .services.category import CagegoryService

class CategoryDetail(BaseView):
    """ View for category page """
    def get(self, request, slug):
        return render(request, 'catalog/category.html',
                      CagegoryService.get_data(slug))
