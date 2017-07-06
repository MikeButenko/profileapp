from profileapp.models import RequestInformation
import datetime
from django.http import response, request
from django.utils import timezone

class RequestMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        entry = RequestInformation(request_method=request.META['REQUEST_METHOD'],
                                   execution_time=timezone.now())
        entry.save()
        return response

