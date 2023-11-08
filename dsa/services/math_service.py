import math

class MathCls:

    # Le Constructeur de le Class    
    def __init__(self):
        return None
    
    def mathFn(x:int, y:int, sm:str):
        if sm=="+":
            return x+y
        elif sm=="-":
            return x-y
        elif sm=="*":
            return x*y
        elif sm=="/":
            if x is not 0 and y is not 0:
                return round(x/y, 3)
            else:
                return "Value can not be 0"
        elif sm == "%":
            return (x * y)/100
    