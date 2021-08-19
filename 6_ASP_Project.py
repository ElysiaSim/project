import pandas as pd
import numpy as np

open = pd.read_excel("IMVA.xls", sheet_name=2)

open1 = open["Periods"].str.split(" ", n = 1, expand = True)
data = open.assign(Period= open1[0])
data.index = data["Period"]
del data["Periods"]

wafniwe = data[['Belgium & Luxembourg','Denmark',
 'Finland', 'France', 'Germany', 'Italy', 'Netherlands', 'Norway',
 'Rep Of Ireland', 'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
 'United Kingdom']]

data = data.loc[(data.Period >= str(1978)) & (data.Period <= str(1987))]
print(len(wafniwe.columns))
print(data)