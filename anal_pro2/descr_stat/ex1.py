# 기술 통계 : 자료를 정리 및 요약하는 기초적인 통계 // 추론통계의 기초 자료로 많이 쓰인다.

# 도수 분포표
import pandas as pd

frame = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex_studentlist.csv')
print(frame.head())
print(frame.shape)
print(frame.info())
print(frame.describe())

# 평균, 분산, 표준 편차, 빈도수, 변수 간의 상관 관계...

# bloodtype 을 나타내는 변수의 빈도 수
data1 = frame.groupby(['bloodtype'])['bloodtype'].count()           # 혈액형별 인원 수 
print(data1)

# bloodytype을 나타내는 변수의 빈도 수 2 crosstab
print('\n One-way tables -----')
data2 = pd.crosstab(index=frame['bloodtype'], columns = 'count')
print(data2)

#
print('\n Two-way tables -----')
data3 = pd.crosstab(index=frame['bloodtype'], columns=frame['sex'])         # 성별 혈액형 별 인원수
print(data3)

print()
data4 = pd.crosstab(index=frame['bloodtype'], columns=frame['sex'], margins = True)         # 소계 인원수
print(data4)
data4.columns = ['남','여','행합']
data4.index = ['A','AB','B','O','열합']
print(data4)


print()
print(data4 / data4.loc['열합','행합']) # 행열 비율
print(data4 / data4.loc['열합']) # 열 비율

print()
print(data4.div(data4['행합'], axis = 0))
print()
print(data4.T / data4['행합'])

# ...
 

