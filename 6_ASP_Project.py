import pandas as pd
import numpy as np

open = pd.read_excel("IMVA.xls", sheet_name=2)

open1 = open["Periods"].str.split(" ", n = 1, expand = True)
data = open.assign(Period= open1[0])
data.index = data["Period"]

data = data.loc[(data.Period >= str(1978)) & (data.Period <= str(1987))]

selected_columns = data[['Belgium & Luxembourg','Denmark',
 'Finland', 'France', 'Germany', 'Italy', 'Netherlands', 'Norway',
 'Rep Of Ireland', 'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
 'United Kingdom']]

print(data.head(3))
print(selected_columns.columns)

for name, values in selected_columns.iteritems():
    print(np.sort('{name}: {value}'.format(name=name, value=values[0]), axis= None))