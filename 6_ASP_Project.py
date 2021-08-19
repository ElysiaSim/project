import pandas as pd
import numpy as np

open = pd.read_excel("IMVA.xls", sheet_name=2)
print(open)

open1 = open["Periods"].str.split(" ", n = 1, expand = True)
data = open.assign(Period= open1[0])
data.index = data["Period"]
del data["Periods"]
print(data.columns)

data = data.loc[(data.Period >= str(1978)) & (data.Period <= str(1987))]
print(data)