from django import template
from django.http import HttpResponse
import json


register = template.Library()

@register.filter
def my_fn(x,y):
    return x+y


@register.simple_tag
def my_fn2(x,y):
    return x+y

@register.simple_tag
def get_url(x):
    return x


@register.simple_tag
def my_fn3(url:HttpResponse):
    if url.status_code == 200:
        return url.photo
    else:
        return "https://www.thecakepalace.com.au/wp-content/uploads/2022/10/dummy-user.png" 