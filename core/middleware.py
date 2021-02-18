from datetime import datetime
from django.db import connection
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class WorkTimeLog:
    """ We use it to log time """
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        start = datetime.now()
        response = self._get_response(request)
        work_time = datetime.now() - start
        logger.debug('Work time: {}'.format(work_time), extra={'method':request.method, 'url': request.build_absolute_uri()})
        if work_time.total_seconds()  > 0.5:
            logger.warning('Work time more than 0.5s: {}'.format(work_time), extra={'method':request.method, 'url': request.build_absolute_uri()})
        return response

class CountQueryLog:
    """ We use it to count queries """
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
        logger.debug('Count queries: {}'.format(len(connection.queries)), extra={'method':request.method, 'url': request.build_absolute_uri()})
        return response

