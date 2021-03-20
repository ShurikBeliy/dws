from django import template

register = template.Library()

@register.simple_tag
def define(val=None):
    """ Return value that was given as an parameter """
    return val
