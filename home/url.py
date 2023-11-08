from django.urls import path
from home import views

urlpatterns = [
   path("",views.static_home, name='home') # function based view
]
