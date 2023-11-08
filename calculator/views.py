import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View



class Calc(View):

    #numbs = [1,2,3,4,5,6,7,8,9,0]
    numbs = [7,8,9,4,5,6,1,2,3,0]
    opt = ['+','-','X','/']

    

    def get(self, request):
        
        
        return render(
            request, 
            "calculator/html/calc.html",
            {
                "num": self.numbs,
                "opt": self.opt
            }
            )

    def post(self):
        pass


# function based view rendering

def funbased_view_1(request:HttpResponse):
    data = jfn()
    my_fn3("https://randomuser.me/api/portraits/men/02.jpg")
    resp = render(   
            request,          
            "calculator/html/customTag.html",
            {
                "msg": "Custom Template",
                "data": data
            }
        )
    print(resp.status_code)
    return resp
    
def jfn():
    file = open("static/data/nestedJsonFile.json").read()
    data = json.loads(file)
    return data

def my_fn3(url):
    return
    



    

