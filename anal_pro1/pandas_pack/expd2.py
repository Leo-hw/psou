# pandas 연습 계속
from pandas import Series, DataFrame

# Series 의 재색인
data = Series(['가', '나', '다'], index=(1, 4, 2))
print(data)
data2 = data.reindex((1,2,4))
print(data2)
# 인덱스를 재배치 하여 순서 변경.

print()

# 재배치 시 값 채우기
data3 = data2.reindex([0,1,2,3,4,5])            # 대응 값이 없는 인덱스는 NaN으로 채워짐.(결측값)
print(data3)

#print(data2.reindex([0,1,2,3,4,5], fill_value=777))         # 대응 값이 없는 경우 채우기
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)
print(data3)

data4 =data2.reindex([0,1,2,3,4,5])            
print(data4.reindex([0,1,2,3,4,5], method='ffill'))         # 대응 값이 없는 경우 채우기
print(data4.reindex([0,1,2,3,4,5], method='pad'))         # 상동

print()
print(data4.reindex([0,1,2,3,4,5], method='bfill'))         # 대응 값이 없는 경우 채우기
print(data4.reindex([0,1,2,3,4,5], method='backfill'))         # 상동


print('---------------------------------------')
import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(12).reshape(4,3), index = ['1월', '2월', '3월','4월'], columns=['강남','강북', '강서'])
print(df)
print(df['강남'])
print(df['강남']>3)                   # '강남' 열의 조건에 맞춰 boolean 출력
print(df[df['강남']>3])           # 조건이 참인 행이 출력되므로 모든 열이 다 나옴.
print()
print(df<3)
df[df<3] =0                             # 조건 참인 녀석을 갱신
print(df)

print('\n DataFrame 관련 슬라이싱 메소드 - loc(), ilox()')
print(df.loc['3월', :])      # '3월' 행 출력
print(df.loc[:'2월'])
print(df.loc[:'2월', ['강서']])    # 2월 이하 행, 강서 열 출력
print()
print(df.iloc[2])           # 2행 출력
print(df.iloc[2,:])

print()
print(df.iloc[:3])
print(df.iloc[:3, 2])
print(df.iloc[:3, 1:3])         # 3행 미만 행, 1,2열 출력
