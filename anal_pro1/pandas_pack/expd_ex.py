'''
Created on 2020. 11. 10.

@author: KITCOOP
'''
import pandas as pd
import numpy as np
from pandas import Series
from dask.dataframe.methods import fillna_check

# 문제 1)
df = pd.DataFrame(np.arange(36).reshape(9,4), columns=['no1','no2','no3','no4'])
#df = pd.DataFrame(np.arange(12).reshape(4,3), index = ['1월', '2월', '3월','4월'], columns=['강남','강북', '강서'])

print(df)
print(df.mean(axis=0))

# 문제2)
df = pd.DataFrame([10,20,30,40],index=['a','b','c','d'], columns=['numbers'])
print(df)
print(df.loc['c'])
print(df.iloc[[0,3]])
print(df.sum())
print(df**2)
print()

df2 = pd.DataFrame(df, index=['a','b','c','d'],columns=['numbers','floats'])
#df2= pd.DataFrame([1.5, 2.5,3.5,4.5], index=['a','b','c','d'])
# seri = Series([1.5,2.5,3.5,4.5], index=['a','b','c','d'], columns=['floats'])
# print(seri)
# df2 = df.insert(seri)

print(df2)

print(df2.isnull())

#df3 = df2.floats.fillna(pd.Series([1.5,2.5,3.5,4.5]))
#df3 = df2[['numbers','floats']].fillna(pd.DataFrame({'numbers':[10,20,30,40], 'floats':[1.5,2.5,3.5,4.5]}))
df3 = df2.fillna(value=1.5, method='ffill', axis=1, inplace=True)
print(df3)
