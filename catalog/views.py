from django.http import HttpResponse
from django.shortcuts import render
from core.views import BaseView
from .services.category import get_active_category_data

class CategoryDetail(BaseView):
    """ View for category page """
    def get(self, request, slug) -> HttpResponse:
        return render(request, 'catalog/category.html',
                      get_active_category_data(slug))

class CategoryList(BaseView):
    """ View for all active categories """
    def get(self, request) -> HttpResponse:
        return render(request, 'catalog/categories.html',{})
