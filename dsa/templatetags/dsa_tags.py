from django import template

register = template.Library()

@register.simple_tag
def mathFn(x,y):
    return x+y
