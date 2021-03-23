from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http.response import Http404
from typing import Union
import logging

logger = logging.getLogger(__name__)

class BaseView(View):
    """ Base view class that try to catch uncaught exceptions and log them """
    def dispatch(self, request, *args, **kwargs) -> Union[HttpResponse, JsonResponse]:
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            extra={'method':request.method, 'url': request.build_absolute_uri()}
            logger.error('Exception is: {}'.format(e), extra=extra)
            raise Http404('The requested URL was not found on this server.')

        if isinstance(response,(dict,list)):
            return self._response(response)
        return response

    @staticmethod
    def _response(data, status=200) -> JsonResponse:
        """ Return json response """
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list)
        )

class IndexDetail(BaseView):
    """ View for index page """
    def get(self, request) -> HttpResponse:
        return render(request, 'index.html', {})

