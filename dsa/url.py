from django.urls import path
from dsa import views

urlpatterns = [
    path("", views.http, name="dsa"),
    path("jsForm/", views.js_form, name="dsa_jsForm"),
    path("pipeFile/", views.pipe_file, name="dsa_pipeFile"),
    path("numpy_1/", views.tuto_numpy, name="dsa_numpy_1"),
]