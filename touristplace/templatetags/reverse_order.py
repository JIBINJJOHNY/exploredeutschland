from django import template

register = template.Library()

@register.filter
def reverse_order(value):
    return 6 - value
