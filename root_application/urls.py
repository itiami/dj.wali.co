"""
URL configuration for root_application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.url")), # function based view
    path("eleve/",include("std_app.url")), # or route all view to std_app.url file
    path("address/",include("address_app.url")), # or route all view to std_app.url file
    path("calc/",include("calculator.url")), # or route all view to std_app.url file
    path("tuto/",include("custom_tags.url")), # or route all view to std_app.url file
    path("dsa/",include("dsa.url")), # or route all view to std_app.url file
]


