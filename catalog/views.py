from django.shortcuts import render
from django.views.generic import View

class IndexDetail(View):
    def get(self, request):
        return render(request, 'catalog/index.html', {})
