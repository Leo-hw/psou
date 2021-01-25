# 연산
from pandas import Series, DataFrame
import numpy as np


s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['a','b','d','c'])
print(s1+s2)            # index명 끼리 연산 - 불일치 할 경우 NaN
print(s1.add(s2))
print(s1 * s2)

print()
df1 = DataFrame(np.arange(9.).reshape(3,3), columns=list('kbs'), index=['서울','대전','부산'])
df2 = DataFrame(np.arange(12.).reshape(4,3), columns=list('kbs'), index=['서울','대전','부산','광주'])
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2))
print(df1.add(df2, fill_value=0))           # NaN은 fill_value 로 채움
# sub, mul, div ...

print()
seri = df1.iloc[0]
print(seri, type(seri))             # pandas.core.series.Series
print(df1 -seri)                        # Series 의 색인을 DataFrame 의 칼럼에 맞추고 아래행으로 전파. Broadcasting

print('~~~~~~' * 10)
# NaN 값 처리
df = DataFrame([[1.4, np.nan],[7,-4.9],[np.NaN, None], [0.5,-1]], columns=['one','two'])
print(df)
print(df.isnull())              # null 여부 확인.
print(df.notnull())
print(df.drop(1))             # 1 행 삭제
print(df.dropna())           # NaN 이 포함된 행 삭제.
print(df.dropna(how='any'))     # NaN 이 하나라도 있으면 
print(df.dropna(how='all'))       # NaN 이 모두 포함 되어 있을 경우만 삭제  
print()
# 기술적 통계와 관련된 연산 메소드
print(df.dropna(axis='columns'))    # NaN이 포함 된 열이 있는 경우 삭제
print(df.dropna(axis='rows'))   #NaN이 포함된 행이 있는 경우 삭제

print(df.dropna(subset=['one']))   # 특정 칼럼에 NaN이 있는 경우 해당 행 삭제
print()
print(df.fillna(0))         # NaN 에 특정 값으로 채우기
print(df.fillna(method='ffill'))

print()
#기술적 통계와 관련된 연산 메소드
print(df.sum())                   # mean, max, min
print(df.sum(axis=0))       # 열 단위 합
print(df.sum(axis=1))       # 행 단위 합
print()
print(df.mean())
print(df.mean(axis=1, skipna = False))
print(df.mean(axis=1, skipna = True))       # 특정 행에 모든 값이 NaN인 경우 NaN

print(df.mean(axis=0, skipna = False))
print(df.mean(axis=0, skipna = True))

print()
print(df.max())                    # 가장 큰 값(맥스값)을 알려줌.
print(df.max(axis=0))
print(df.idxmax())              # 맥스 값이 있는 위치를 알려줌.( value 값 중 max 값을 가진 곳의 index 를 반환)
print(df.idxmax(axis=0))

# 요약 통계량
print(df.describe())
print(df.info())        # 구조 출력

print()
dfwords = DataFrame(['봄','여름','가을','봄'])
print(dfwords.describe())
print(dfwords.info())







