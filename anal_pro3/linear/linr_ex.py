# 회귀분석 문제 1) scipy.stats.linregress(), statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균값을 사용하기로 한다. 운동 칼럼에 대해 이상치가 있는 행은 제거.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt  
import urllib.request

#url = 'C:/work/psou/anal_pro3/linear/tvpro.txt'
data = np.genfromtxt('C:/work/psou/anal_pro3/linear/tvpro.txt', delimiter=',', encoding='utf-8')
#print(data)
df = pd.DataFrame(data, columns=['구분','지상파','종편','운동'])
df = df.dropna()

print(df.head())

x = df['지상파']
y = df['운동']
z = df['종편']

print(np.corrcoef(x,y))
print(df.corr())
model = stats.linregress(x, y)
print(model)
print('기울기 : ', model.slope)
print('절편 : ', model.intercept)
print('상관계수 : ', model.rvalue)
print('결정계수 : ', model.rvalue**2)
print('p-value : ', model.pvalue)
print('표준오차 : ', model.stderr)

ndf = float(input('입력하세요'))
newdf = pd.DataFrame({'지상파':[ndf]})
print(newdf)
print(np.polyval([model.slope, model.intercept], newdf))
