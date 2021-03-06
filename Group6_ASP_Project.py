import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

open = pd.read_excel("IMVA.xls", sheet_name=2)
open1 = open["Periods"].str.split(" ", n = 1, expand = True)
data = open.assign(Period= open1[0])
data.index = data["Period"]
data1 = data.loc[(data.Period >= str(1978)) & (data.Period <= str(1987))]

colExtra = data1.filter(items=['Periods','Belgium & Luxembourg','Denmark',
 'Finland', 'France', 'Germany', 'Italy', 'Netherlands', 'Norway',
 'Rep Of Ireland', 'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
 'United Kingdom'])
print(colExtra.head(3))
print(colExtra.tail(3))

col = data1.filter(items=['Belgium & Luxembourg','Denmark',
 'Finland', 'France', 'Germany', 'Italy', 'Netherlands', 'Norway',
 'Rep Of Ireland', 'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
 'United Kingdom'])


print(col.columns)

col = col.replace(',', '', regex= True)
col = col.replace('na', 0, regex= True)
col = col.astype(int)
total = col.sum(axis=0)
totalsum = total.sort_values(ascending=False)
top3e = sum(totalsum.head(3))
top3Mean = round(totalsum.head(3).mean(), 2)

print("\n-------Sorted Countries-------")
print(totalsum)
print("\n-------Top 3 Countries-------")
print(totalsum.head(3))
print("The total no. of visitors for the top 3 countries is", top3e)
print("The mean value for the top 3 countries is", top3Mean)
print("\n---------Indexes of Countries---------")
print(col.columns)

col.index = col.index.astype(int)

def allCountry():
    print("\nAll Country Chart:")
    y = total.sort_values(ascending=False)
    x = np.arange(len(y.index))
    plt.xlabel('Countries', fontsize=13)
    plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
    plt.xticks(x, y.index, fontsize=11, rotation=90)
    plt.title('Europe1 (Period: 1978 - 1987)')
    plt.bar(y.index, y.values)
    plt.savefig("Europe1")
    plt.show()

def top3():
    y = totalsum.head(3)
    x = np.arange(len(y.index))
    print("\nTop 3 Chart:")
    plt.xlabel('Countries', fontsize=13)
    plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
    plt.xticks(x, y.index, fontsize=11, rotation=90)
    plt.title('Europe1 Top3 (Period: 1978 - 1987)')
    plt.bar(y.index, y.values)
    plt.savefig("Europe1_Top3")
    plt.show()

allCountry()
top3()