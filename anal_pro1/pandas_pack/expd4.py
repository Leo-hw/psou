'''
Created on 2020. 11. 10.

@author: KITCOOP
'''
# dataFrame 의 모양 관련 작업
import numpy as np
import pandas as pd

# 행/열 전환, 인덱스 기준 쌓기
df = pd.DataFrame(1000+ np.arange(6).reshape(2,3), index=['대전','서울'], columns=['2017','2018','2019'])
print(df)

print(df.T)
df_row = df.stack()
print(df_row)
df_col = df_row.unstack()
print(df_col)

print()
# 범주화(cut)
price = [10.3, 5.5, 7.8, 3.6]
cut = [3,7,9,11]        # 구간 기준 값
result_cut = pd.cut(price, cut)
print(result_cut)       # (3,7] (a,b] => a < x <= b
print(pd.value_counts(result_cut))

# Series 
datas = pd.Series(np.arange(1, 1001))
print(datas.head(5))
print(datas.tail())

result_cut2 = pd.qcut(datas, 3)
print(result_cut2)
print(pd.value_counts(result_cut2))

print('\n\n 자료 합치기 - DataFrame 병합 -----------------')
df1 = pd.DataFrame({'data1': range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)

print()
print(pd.merge(df1, df2, on = 'key'))           # key 를 기준으로 병합.        inner join
print(pd.merge(df1, df2, on = 'key', how='inner'))           # on = 'key', how = 'inner'
print(pd.merge(df1, df2, on = 'key', how='outer'))          # 정수는 실수화...why(?) // full outer join
print()
print(pd.merge(df1, df2, on = 'key', how='left'))           # left outer join
print(pd.merge(df1, df2, on = 'key', how = 'right'))        # right outer join

print() # 공통 칼럼 명이 없는 경우
df3 = pd.DataFrame({'key2':['a','b','d'], 'data2':range(3)})
print(df3)
print(pd.merge(df1, df3, left_on = 'key', right_on = 'key2'))       # inner join

print()
print(pd.concat([df1,df3]))         # 자료 이어 붙이기.
print(pd.concat([df1,df3], axis=0))
print()
print(pd.concat([df1,df3], axis=1))

#Series 도 가능
# numpy 의 ndarray 는 np.concatenate()
