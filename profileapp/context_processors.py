from django.conf import settings
from profileapp.models import models

def context_proc(request):
    return {
        'settings': settings,
        'ip_address': request.META['REMOTE_ADDR'],
        'mime': request.META['CONTENT_TYPE']
    }


def get_models_object(request):
    pass