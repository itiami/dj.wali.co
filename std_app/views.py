import json
import os
from datetime import datetime
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .std_model.student import Student


# this is function based view that render html content
# and this function forwarded to url.py urlpatterns[] list which again forwarded to the project level urls.py
# which get loaded by settings.py ROOT_URLCONF = 'root_application.urls' and which gets load on application start
# from manage.py under main() function.. os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root_application.settings')
# so the routing is ..
# manage.py > root_application.settings.py > root_application.urls > std_app.url.py > std_app.views.py > std_app.template.index.html etc.

# View rendering can be done by using function or class

# function base view rendering
# def home(x):
#     content = "<html><body><h3>Hi.. it's Me Wali</h3></body></html>"
#     return HttpResponse(content)

# class base view rendering


class Std(View):

    student = Student()

    def get(self, request):

        return render(
            request,
            "std_app/html/std_app.html",
            {
                "msg": "Salut, je suis à l'intérieur de la fonction",
            }
        )

    def post(self, rq: HttpRequest):
        obj = {
            "pnom": rq.POST['prenom'],
            "nom": rq.POST.get('lname'),
            "dob": rq.POST['dob'],
            "email": rq.POST['email'],
            "phone": rq.POST['phone'],
        }

        return render(
            rq,
            "std_app/html/data.html",
            {
                "msg": "Salut, je suis à l'intérieur de la fonction",
                "full": json.dumps(obj, indent=2),
                "data": json.dumps(pourforloop(), indent=2)
            }
        )

    def setStd():
        wali = Student("Abdullah", "Wali", "06524125")
        return wali


######################## Function based views ################################
def veu_sur_fon(rq: HttpRequest):
    if rq.method == 'POST':
        obj = {
            "pnom": rq.POST['prenom'],
            "nom": rq.POST.get('lname'),
            "dob": rq.POST['dob'],
            "email": rq.POST['email'],
            "phone": rq.POST['phone'],
        }
        return render(
            rq,
            "std_app/html/data.html",
            {
                "msg": "Salut, je suis à l'intérieur de la fonction",
                "full": json.dumps(obj, indent=2),
                "data": json.dumps(pourforloop(), indent=2)
            }
        )

    if rq.method == 'GET':
        print(get_type(pourforloop()))

        resp = render(
            rq,
            "std_app/html/data.html",
            {
                "msg": "Salut, je suis à l'intérieur de la fonction",
                # "full": fullName,
                "data": json.dumps(pourforloop(), indent=2)
            }
        )
        return resp


def pourforloop():
    obj = {
        'nom': 'wali',
        'prenom': 'affi',
        'age': 15,
        'il_a': [
            'telephone',
            'pc',
            'velo',
            'passion de travail'
        ]
    }

    return obj


def get_type(x):
    # return type(x) # <class 'dict'>
    return isinstance(x, dict)  # True
