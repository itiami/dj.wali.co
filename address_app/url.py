from django.urls import path, include
from address_app import views

urlpatterns = [
    path("", views.getAddress, name="getAddr"),  # function based view
    path("add/", views.insAddress, name="insAddr")  # function based view
]
