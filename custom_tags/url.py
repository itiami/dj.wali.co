from django.urls import path
from custom_tags import views

# function and class based view
# here name param is use to send the path[0] to the html template to create href link, 
# this path() act as a tuple() type list...
urlpatterns = [
   path("",views.Sys.as_view(), name = "ul_li"),
   path("tbl/",views.sys_info, name = "render_data_tbl"),
   path("list/",views.list_data, name ="list_data"),
   path("json/",views.nested_json, name ="nested_json"),

]