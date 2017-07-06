from django import template
from ..models import Profile

register = template.Library()


@register.simple_tag
def total_objects():
    for obj in Profile.objects.filter().values('id', 'first_name',
                                               'last_name', 'date_of_birth',
                                               'biography','contacts'):

        return obj
