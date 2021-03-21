from datetime import datetime
from django.db import connection
from django.http import HttpResponse, JsonResponse
from typing import Union
import logging

logger = logging.getLogger(__name__)

class WorkTimeLog:
    """ We use it to log time """
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request) -> Union[HttpResponse, JsonResponse]:
        start = datetime.now()
        response = self._get_response(request)
        work_time = datetime.now() - start
        extra={'method':request.method, 'url': request.build_absolute_uri()}
        logger.debug('work time: {}'.format(work_time), extra=extra)
        # add warning logs for pages that are slow
        if work_time.total_seconds()  > 0.5:
            logger.warning('work time > 0.5s: {}'.format(work_time), extra=extra)
        return response

class CountQueryLog:
    """ We use it to count queries """
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request) -> Union[HttpResponse, JsonResponse]:
        response = self._get_response(request)
        cnt_queries=len(connection.queries)
        extra={'method':request.method, 'url': request.build_absolute_uri()}
        logger.debug('Page has {} queries'.format(cnt_queries), extra=extra)
        #add warning for pages that have more than 10 queries
        if cnt_queries > 9:
            logger.warning('Page has {} queries that more than 10'.format(cnt_queries), extra=extra)
        return response

