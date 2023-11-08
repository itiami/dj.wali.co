from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path


def static_home(request: HttpRequest):
    resp = render(
        request,
        "home.html",
        {
            "adminPath": request.get_host(),
            "data": menu()
        }
    )

    return resp


def menu():
    pages = [
        {
            "pageTitle": "Admin",
            "pageLink": "/admin",
            "isRootLevel": True,
            "hasSubPage": False
        },
        {
            "pageTitle": "Contact",
            "pageLink": "/contact",
            "isRootLevel": True,
            "hasSubPage": False
        },
        {
            "pageTitle": "Les Apps",
            "pageLink": "#",
            "isRootLevel": True,
            "hasSubPage": True,
            "subPages": [
                {
                    "pageTitle": "Home",
                    "pageLink": "{% url 'home' %}",
                    "hasSubPage": False
                },

                {
                    "pageTitle": "Calculator App",
                    "pageLink": "#",
                    "hasSubPage": True,
                    "subPages": [
                        {
                            "pageTitle": "Calculator",
                            "pageLink": "{% url 'calc' %}",
                        },

                        {
                            "pageTitle": "Calc Page_2",
                            "pageLink": "{% url 'calc2nd' %}",
                        },

                    ]
                },

                {
                    "pageTitle": "Eleve App",
                    "hasSubPage": True,
                    "subPages": [
                        {
                            "pageTitle": "Eleve Home",
                            "pageLink": "{% url 'StdHome' %}",
                        },

                        {
                            "pageTitle": "Eleve 2nd Page",
                            "pageLink": "{% url 'StdFon' %}",
                        },

                    ]
                },
                {
                    "pageTitle": "Car App",
                    "hasSubPage": True,
                    "subPages": [
                        {
                            "pageTitle": "Eleve Home",
                            "pageLink": "{% url 'StdHome' %}",
                        },

                        {
                            "pageTitle": "Eleve 2nd Page",
                            "pageLink": "{% url 'StdFon' %}",
                        },

                    ]
                },
            ]
        },



    ]

    return pages
