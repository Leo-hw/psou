# http://cafe.daum.net/flowlife/RUrO/129
# 회귀분석 문제 1) scipy.stats.linregress(), statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균값을 사용하기로 한다. 운동 칼럼에 대해 이상치가 있는 행은 제거.

import pandas as pd
import numpy as np

# DataFrame화
txt = np.genfromtxt('linear_ex.txt', delimiter=',', encoding = 'utf8')[1:]
data = pd.DataFrame(txt)
data.columns = ['구분','지상파','종편','운동']
# print(data)

# 결측치 확인 및 전처리 작업
# print(data.isnull().sum())
data.지상파 = data.지상파.fillna(data.지상파.mean())
# data.운동 = data.운동.dropna(axis=1) ## 이거 안돼?
# print(data)

# 예측 해야할 statement 
#     - 지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 (Q1)
#     - 지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 (Q2)

# 독립 변수와 종속 변수 설정
x_ground = data.지상파
y_exercise = data.운동
y_final = data.종편

## 상관관계 확인
print(np.corrcoef(x_ground, y_exercise)) # 약한 상관 관계
print(np.corrcoef(x_ground, y_final)) # 강한 상관 관계
print(data[['지상파', '종편', '운동']].corr())

# 입력받을 지상파 시청 시간
ground_time = float(input('지상파 시청시간 입력:'))

# 모델1: scipy.stats.linregress()
from scipy import stats
model_exercise = stats.linregress(x_ground, y_exercise)
model_final = stats.linregress(x_ground, y_final)
# print(model)
print('scipy.stats.linregress()로 예측한 값 ↓')
print('예측 운동시간:', np.polyval([model_exercise.slope, model_exercise.intercept],
                             ground_time))
print('예측 종편 시청 시간:', np.polyval([model_final.slope, model_final.intercept],
                             ground_time))

# 모델2: statsmodels ols()
import statsmodels.formula.api as smf

data = np.array([x_ground, y_exercise])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']
# print(df.head())

model2_exercise = smf.ols(formula = 'y1 ~ x1', data=df).fit()

data = np.array([x_ground, y_final])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']

model2_final = smf.ols(formula = 'y1 ~ x1', data=df).fit()
print('statsmodels ols()로 예측한 값 ↓')
print('예측 운동시간:', model2_exercise.predict({'x1': ground_time}))
print('예측 종편 시청 시간:', model2_final.predict({'x1': ground_time}))

# 모델3: LinearRegression (* 미완성
from sklearn.linear_model import LinearRegression


model = LinearRegression()
model3_exercise = model.fit(x_ground.values.reshape(-1,1), y_exercise)
print('LinearRegression()로 예측한 값 ↓')
print('예측 운동시간:', model3_exercise.predict(x_ground.values.reshape(-1,1))) # x 형태가 바뀌어 버림

model3_final = model.fit(x_ground.values.reshape(-1,1), y_final)
print('예측 종편 시청 시간:', model3_final.predict(x_ground.values.reshape(-1,1)))