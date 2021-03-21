from django import template

register = template.Library()

@register.simple_tag
def define(val=None) -> any:
    """ Return value that was given as an parameter """
    return val
