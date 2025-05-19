from django import template

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """
    Split a string by the given delimiter and return a list.
    Usage: {{ value|split:"," }}
    """
    if not value:
        return []
    return value.split(delimiter)
