from django import template

register = template.Library()

@register.filter
def extract_numeric_value(value):
    return int(''.join(filter(str.isdigit, value)))
