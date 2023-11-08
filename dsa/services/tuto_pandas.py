import csv
from root_application.settings import STATIC_URL
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbrn


class Tuto_Pandas:

    def __init__(self, 
                 csvFile = STATIC_URL + "data/sales_data.csv",
                 pipeFile = STATIC_URL + "data/pipeFile.txt"
                 ):
        self.csvFile = csvFile
        self.pipeFile = pipeFile

    def read_file(self):    
        file = STATIC_URL + "data/pipeFile.txt"
        data = open(self.pipeFile, "r")
        lines = csv.reader(data, delimiter="|")
        return lines

    def pipecontent(self):
        pre = 'col_'

        df_2 = pd.read_csv(
            "static/data/pipeFile.txt", sep='|',
            encoding='unicode_escape',
            engine='python',
            # names=['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7',
            #      'col_8', 'col_9', 'col_10', 'col_11', 'col_12', pre],
            header=None,
        ).add_prefix(pre)

        print(df_2.shape)         
        tblDt=df_2.head(100)
        #print(tblDt)    
        #print(".............tblDt.loc................")    
        #print(tblDt.loc[3])
        print(".............DataFrame................")
        pndf = pd.DataFrame(df_2)
        print(pndf.head(10))
        forSE_1 = pndf[pndf["col_0"].eq("SE1")]
        #print(forSE_1[['col_2','col_3','col_4']])
        se1WithoutNull = forSE_1[['col_3']].head(51).dropna(axis=1,how='all')
        print(se1WithoutNull)

        return df_2

