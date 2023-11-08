from django.urls import path
from std_app import views

urlpatterns = [
   path("",views.Std.as_view(), name="StdHome"), # class based view
   path("fon/",views.veu_sur_fon, name="stdFon") # function based view
]