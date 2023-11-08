from django.urls import path, include
from calculator import views

urlpatterns = [
   path("",views.Calc.as_view(), name = "calc"), # class based view
   path("customTag/",views.funbased_view_1, name= "calc2nd") # class based view
]