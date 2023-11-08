from django.http import HttpRequest
from django.shortcuts import render
from root_application.settings import STATIC_URL
import csv
from .services.math_service import MathCls
from .services.tuto_pandas import Tuto_Pandas
from .services.tuto_num_1 import TutoNum
from time import time
import pandas as pd
from matplotlib import pyplot as plt


tutoPandas = Tuto_Pandas()
tutoNum = TutoNum()


def http(req: HttpRequest):
    num1 = req.POST.get('num_1')
    num2 = req.POST.get('num_2')
    sgn = req.POST.get('symb')

    if (
        num1 is not None and
        num2 is not None and
        len(num1) != 0 and
        len(num2) != 0
    ):
        res = MathCls.mathFn(int(num1), int(num2), str(sgn))
        print(type(res))

    else:
        res = "Please Put values in both Field"

    if req.method == "GET":
        return render(
            req,
            "dsa/html/math_post.html",
            {
                "msg": "On Page Load by GET Request: "
            }
        )

    if req.method == "POST":
        return render(
            req,
            "dsa/html/math_post.html",
            {
                "msg": "This is POST request rendering: ",
                "mathRes": res,
                "sin": sgn
            }
        )


def js_form(req: HttpRequest):
    lst = ["item_1", "item_2", "item_3", "item_4"]
    if req.method == "GET":
        return render(
            req,
            "dsa/html/jsForm.html",
            {
                "data": "hi from views.py",
                "list": lst,
            }
        )

    if req.method == "POST":
        return render(
            req,
            "dsa/html/jsForm.html",
        )


def pipe_file(req: HttpRequest):

    if req.method == "GET":
        return render(
            req,
            "dsa/html/pipeFile.html",
            {
                "title": "Pipe Delimited  Files",
                "col": range(4),
                "pipeData": tutoPandas.pipecontent().head(10),
                "pipeDataSingleRow": ""
            }
        )

    if req.method == "POST":
        return None


def tuto_numpy(req: HttpRequest):
    # print(TutoNum.tuto_1())
    tutoNum.readCsv()

    if req.method == "GET":
        return render(
            req,
            "dsa/html/tuto_num_1.html",
            {
                "title": "Numpy Tutorial"
            }

        )
