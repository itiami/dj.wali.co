import httpx
import asyncio
import os
import time
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
import json

# Class Based Routing...

class Sys(View):

    def __init__(self):
        self.sysLoginUser = os.getlogin
        #self.sysEnv = os.getenv()
        self.sysEnv = os.environ
        self.sysExecPath = os.get_exec_path()
        self.sysUser = os.environ.get('USERNAME')
        self.workingDir = os.path.dirname(os.path.abspath(__file__))
        self.userProfile = os.environ.get('USERPROFILE')
        self.templateName = "custom_tags/html/sys_ul_li.html"

    # sample get Request
    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().get(request, *args, **kwargs)

   

    # Working get request is as below..
    def get(self, request, *arg, **kwargs):
        
        return render(
                request, 
                "custom_tags/html/sys_ul_li.html",
                {
                "SysUserName": self.sysLoginUser,
                "sysEnv": self.sysEnv.items(), # to get key and valu. else self.sysEnv
                "sysExecPath": self.sysExecPath,
                "user": self.sysUser,
                "workingFilePath": self.workingDir,
                "userProfile": self.userProfile,
                }
            ) 
    

    def status_code(x):
        res = httpx.get(x)
        if res.status_code == 200:
            return True
        else:
            return False

    async def test_async(x):
        async with httpx.AsyncClient() as client:
            response = await client.get(x)
            print(response)
            #print(response.status_code)
    
    def loop_data(x):
        for x in x:
            asyncio.run(Sys.test_async(x["photo"]))  


# http://192.168.1.235/tuto/json/
def nested_json(request:HttpRequest): 
    start = time.time() 
    # method_1
    file = open("static/data/nestedJsonFile.json").read()
    jLoad = json.loads(file)
    # # method_2
    # with open("static/data/test.json") as joFile:
    #     data = json.load(joFile)
    #     #print(data[0]["fname"]) # Norma

    #     for x in data:
    #         print(x["fname"])
    
    #Sys.loop_data(jLoad)

    return HttpResponse(
            render(
                    request,
                    "custom_tags/html/nestedJson.html",
                    {
                        "dataList" : jLoad,
                        "img":"https://www.thecakepalace.com.au/wp-content/uploads/2022/10/dummy-user.png",
                        "end": (time.time() - start) * 10**3
                    }
                )
            )

# Function Based Routing..
sys = Sys()
def sys_info(request):
    print(os.getcwd()) # D:\Python\PaPy
    print(os.path.dirname(os.path.abspath(__file__))) # D:\Python\PaPy\custom_tags
    if request.method == "GET":
        #print(request.method) # output GET
        return render(   
                request,          
                "custom_tags/html/sysTbl.html",
                {
                    "SysUserName": sys.sysLoginUser,
                    "sysEnv": os.environ.items(), # to get key and valu. else self.sysEnv
                    "sysExecPath": sys.sysExecPath,
                    "user": sys.sysUser,
                    "workingFilePath": sys.workingDir,
                    "userProfile": sys.userProfile,
                }
            )


def list_data(request): 
    jObj = json.dumps(json_list(), sort_keys=True, indent=3)

    listKeyVal = list_idx(list_fn())
    # output...
    # [{'sn': 0, 'itm': 'listItem_201'}, {'sn': 1, 'itm': 'listItem_202'}, {'sn': 2, 'itm': 'listItem_203'}]
    toJsonObjList = json.dumps(list_idx(list_fn()), sort_keys=True, indent=3)
    # output.. 
    # [{"sn": 0, "itm": "listItem_201"}, {"sn": 1, "itm": "listItem_202"}, {"sn": 2, "itm": "listItem_203"}]
    print(listKeyVal)
    print(toJsonObjList)

    return HttpResponse(
            render(
                    request,
                    "custom_tags/html/list.html",
                    {
                        "dataList" :list_fn(),
                        "jsonObj" : jObj,
                        "jsonListFn" : json_list(),
                        "toJsonObjList" : toJsonObjList,
                        "loadFromJsonObjList" : json.loads(toJsonObjList),
                    }
                )
            )



def list_fn():    
    list = ["DataItem_201","DataItem_202","DataItem_203"]
    return list



def list_idx(listArg:list):
    listAvecIndex = []
    for x in listArg:
        listAvecIndex.append(
            {"sn" : listArg.index(x) ,"itm": x}            
        )
    return listAvecIndex


def json_list():
    json_object_list = [
        {"name": "Item 1", "price": 10},
        {"name": "Item 2", "price": 20},
    ]
    
    return json_object_list







