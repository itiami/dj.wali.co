import numpy as np
from root_application.settings import STATIC_URL

class TutoNum:

    def __init__(self, 
                 csvFile = STATIC_URL + "data/sales_data.csv",
                 pipeFile = STATIC_URL + "data/pipeFile.txt"
                 ):
        self.csvFile = csvFile
        self.pipeFile = pipeFile

    def tuto_1():
         npArr()
         np3DArr()

    def readCsv(self):
        fileByStaticUrl = STATIC_URL + "data/pipeFile.txt"
        # or
        f = 'static/data/sales_data.csv'
        csvFile = np.loadtxt(f, dtype=object, delimiter=",", unpack=True, skiprows=1, max_rows=5)
        #id, names, pId, gender, ageGroup, age = csvFile
        (uId,cName,pId,gender,ageGroup,age,status,civilState,
         zone,job,pCat,orders,amount,status,unnamed1) = csvFile
        print(csvFile)
        print(uId)
        
     
             
        return csvFile
         

                
def npArr():
    T = np.array([5, 2, 8, 17, 6, 14])
    print(T) # [ 5  2  8 17  6 14]
    print(np.sort(T)) # [ 2  5  6  8 14 17]
    T1 = np.arange(15)
    print(T1) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    T2 = np.arange(0.9, 8.1, 0.5)
    print(T2) # [0.9 1.4 1.9 2.4 2.9 3.4 3.9 4.4 4.9 5.4 5.9 6.4 6.9 7.4 7.9]
    T3 = np.linspace(0, 1/4, 16)
    print(T3)


def np2dArr():
    arr = np.array(
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
    )

    for x in arr:
            for dt in x:
                print(dt)


def np3DArr():
    arr = np.array(
        [
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            [
                [7, 8, 9],
                [10, 11, 12]
            ]
        ]
    )

    # for x in arr:
    #      for x2 in x:
    #           for x3 in x2:
    #                print(x3)

    for x in np.nditer(arr):
        print(x)
              
         
def npFilter():
    arr = np.array([41, 42, 43, 44, 45])
    x = arr[[True, False, True, True, False]]
    print(x) # [41 43 44]




