from django.shortcuts import render
from core.views import BaseView

class CategoryDetail(BaseView):
    """ View for index page """
    def get(self, request, slug):
        raise Exception("noname")
        return render(request, 'catalog/category.html', {})
