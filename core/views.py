from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import logging

logger = logging.getLogger(__name__)

class BaseView(View):
    """ Base view class that try to catch uncaught exceptions and log them """
    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            extra={'method':request.method, 'url': request.build_absolute_uri()}
            logger.error('Exception is: {}'.format(e), extra=extra)
            return redirect('page_404_url')

        if isinstance(response,(dict,list)):
            return self._response(response)
        return response

    @staticmethod
    def _response(data, status=200):
        """ Return json response """
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list)
        )

class Page404Detail(BaseView):
    """ View for page 404 """
    def get(self, request):
        response = render(request, '404.html', {})
        response.status_code = 404
        return response

class IndexDetail(BaseView):
    """ View for index page """
    def get(self, request):
        return render(request, 'index.html', {})
