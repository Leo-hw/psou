# 그룹화 : groupby, pivot, pivot_table
# 피벗테이블 : 데이터 열 중에서 두 개의 열을 사용하여 데이터 테이블의 행렬을 재구성

import numpy as np
import pandas as pd

data = {'city':['강남','강북','강남','강북'],
        'year':[2000, 2001, 2002, 2002],
        'pop':[3.3, 2.5, 3.0, 2.0]
        }

df = pd.DataFrame(data)
print(df)

print()
print(df.pivot('city', 'year', 'pop'))
print()         # set_index 기존의 행 인덱스를 제거하고 첫번째 열 인덱스를 설정
print(df.set_index(['city','year']).unstack())

print(print(df.pivot('year','city','pop')))
print(df.set_index(['year','city']).unstack())

print(df['pop'].describe())         # 요약 통계량 출력

print()

hap = df.groupby(['city'])
print(hap.sum)      

print(df.groupby(['city']).sum())           # 위 두 줄과 동일.
print(df.groupby(['city', 'year']).mean())

print('\npivot_table() : pivot 과 groupby 의 중간적 성격')
print(df.pivot_table(index = ['city']))
print(df.pivot_table(index = ['city'], aggfunc=np.mean))        # 상동
print(df.pivot_table(index = ['city'], aggfunc=np.std))
print(df.pivot_table(index = ['city','year'], aggfunc=np.mean))
print(df.pivot_table(index = ['city','year'], aggfunc=[np.mean, np.sum, len]))
print()
print(df.pivot_table(values=['pop'], index = 'city'))
print(df.pivot_table(values=['pop'], index = 'city',aggfunc=len))
print()
print(df.pivot_table(values=['pop'], index = ['year'], columns=['city']))
print(df.pivot_table(values=['pop'], index = ['year'], columns=['city'], margins=True))
print(df.pivot_table(values=['pop'], index = ['year'], columns=['city'], margins=True, fill_value=0))