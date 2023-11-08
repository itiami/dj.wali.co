# customFn.py 
import asyncio
import time
from django import template
from django.http import HttpResponse
import httpx
import requests
import urllib3
from django.http import JsonResponse

register = template.Library()

@register.simple_tag
def multi(arg1, arg2):
    return arg1 * arg2

@register.simple_tag
def division(arg1, arg2):
    return arg1 / arg2


# to call in html template means html file
# <div>{{ 4|multiply:5 }}</div>

def current_milli_time():
    return round(time.time() * 1000)

@register.filter
def substruction(arg1, arg2):
    return arg1 - arg2

@register.filter
def get_img_filter(str):
    url = urllib3.request("get", str, timeout=1)
    if url.status == 200:
        return str
    else:
        return "https://www.thecakepalace.com.au/wp-content/uploads/2022/10/dummy-user.png" 

@register.simple_tag
def get_img_lib3(str):
    url = urllib3.request("get", str, timeout=1)
    if url.status == 200:
        return str
    else:
        return "https://www.thecakepalace.com.au/wp-content/uploads/2022/10/dummy-user.png" 
    
@register.simple_tag
def get_img_requests(str):
    url = requests.head(str, timeout=1)
    if url.status_code == 200:
        return str
    else:
        return "https://www.thecakepalace.com.au/wp-content/uploads/2022/10/dummy-user.png" 
    

@register.filter
def get_code(x):
    url = requests.head(x)
    return url.status_code

@register.simple_tag
def getLst():
    ls=[1,2,3,"test"]
    return ls


async def test_async(x):
    async with httpx.AsyncClient() as client:
        response = await client.get(x)
        #print(response)
        #print(response.status_code)
        return response.status_code

@register.simple_tag
def async_httpx(x):   
    scode = asyncio.run(test_async(x))
    if scode == 200:
        return x
    else:
        return "https://www.thecakepalace.com.au/wp-content/uploads/2022/10/dummy-user.png" 

async def http_call_async():
  for num in range(1,6):
    await asyncio.sleep(1)
    print(num)
  async with httpx.AsyncClient() as client:
    r = await client.get("https://httpbin.org")
    print(r)