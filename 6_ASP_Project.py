import pandas as pd
import numpy as np

open = pd.read_excel("IMVA.xls", sheet_name=2)
print(open)

open1 = open["Periods"].str.split(" ", n = 1, expand = True)
data = open.assign(Years= open1[0])
data.index = data["Years"]
del data["Periods"]


data = data.loc[(data.Years >= str(1978)) & (data.Years <= str(1987))]
print(data)