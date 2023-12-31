import random

from django import template

register = template.Library()


@register.simple_tag
def break_cache():



    return random.randint(0, 50000)