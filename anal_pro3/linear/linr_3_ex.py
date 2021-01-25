# 회귀분석 문제 1) scipy.stats.linregress(), statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균값을 사용하기로 한다. 운동 칼럼에 대해 이상치가 있는 행은 제거.
# 구분,지상파,종편,운동
# 1,0.9,0.7,4.2
# 2,1.2,1.0,3.8
# 3,1.2,1.3,3.5
# 4,1.9,2.0,4.0
# 5,3.3,3.9,2.5
# 6,4.1,3.9,2.0
# 7,5.8,4.1,1.3
# 8,2.8,2.1,2.4
# 9,3.8,3.1,1.3
# 10,4.8,3.1,35.0
# 11,NaN,3.5,4.0
# 12,0.9,0.7,4.2
# 13,3.0,2.0,1.8
# 14,2.2,1.5,3.5
# 15,2.0,2.0,3.5
from scipy import stats
import numpy as np
import pandas as pd

gubun = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
jisang = [0.9,1.2,1.2,1.9,3.3,4.1,5.8,2.8,3.8,4.8,None,0.9,3.0,2.2,2.0]
jong = [0.7, 1.0, 1.3, 2.0, 3.9, 3.9, 4.1, 2.1, 3.1, 3.1, 3.5, 0.7, 2.0, 1.5, 2.0]
undong = [4.2, 3.8, 3.5, 4.0, 2.5, 2.0, 1.3, 2.4, 1.3, 35.0, 4.0, 4.2, 1.8, 3.5, 3.5]
ex1 = pd.DataFrame({'구분' : gubun, '지상파' : jisang, '종편' : jong, '운동' : undong})
#print(ex1)
print("지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.")
# 지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.

ex1 = ex1.fillna(ex1['지상파'].mean()) # 결측치 평균값으로 채우기
#print(ex1)
ex1 = ex1.drop(9) # 이상치 제거
print(ex1)
x = ex1.지상파
y = ex1.운동

# 상관계수
print(ex1.corr()) # -0.865535 음의상관관계
model = stats.linregress(x, y)
print(model)
print('기울기 : ', model.slope)
print('절편 : ', model.intercept)
print('상관계수 : ', model.rvalue)
print('결정계수 : ', model.rvalue ** 2)
print('유의확률(p-value) : ', model.pvalue)
print('표준오차 : ', model.stderr)

print('운동시간예측 :', model.slope * 5.5 + model.intercept)
print('운동시간예측 :', model.slope * 1.5 + model.intercept)
# 지상파 시청시간이 늘수록 운동시간이 낮아지는것을 확인

print('\n지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.')
#  - 지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
x2 = ex1.지상파
y2 = ex1.종편
#print(ex1.corr()) # 0.887530 양의 상관관계
model2 = stats.linregress(x2, y2)
print('기울기 : ', model2.slope)
print('절편 : ', model2.intercept)
print('상관계수 : ', model2.rvalue)
print('결정계수 : ', model2.rvalue ** 2)
print('유의확률(p-value) : ', model2.pvalue)
print('표준오차 : ', model2.stderr)

print("종편시청 시간 예측 : ", model2.slope * 0.5 + model.intercept)
print("종편시청 시간 예측 : ", model2.slope * 5.5 + model.intercept)
# 지상파 시청시간이 늘어날 수록 종편시청 시간도 늘어나는것을 확인.

