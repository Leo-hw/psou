# (continued)
# 선형 회귀 방법 4 - linear regression(): 모델 있음
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IQ에 따른 시험점수 값 예측
score_iq = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/score_iq.csv')
print(score_iq.head())
print(score_iq.info()) # 모두 int type → 연속형

x = score_iq.iq # 독립 변수
y = score_iq.score # 종속 변수

# 상관 관계 확인
print(np.corrcoef(x, y)) # numpy로 상관관계 확인
# print(score_iq.corr())
print(score_iq[['iq','score']].corr()) # pandas로 상관 관계 확인
# plt.scatter(x, y)
# plt.show() # 인과 관계가 있는 걸로 확인

# IQ가 score에 영향을 준다고 가정 (인과관계가 있으므로 회귀분석이 가능)
model = stats.linregress(x, y)
print(model)
# LinregressResult(slope=0.6514309527270075, intercept=-2.8564471221974657, rvalue=0.8822203446134699, pvalue=2.8476895206683644e-50, stderr=0.028577934409305443)
print('기울기:', model.slope)      # 0.6514309527270075
print('절편:', model.intercept)   # -2.8564471221974657
print('상관계수:', model.rvalue)   # 0.8822203446134699
print('결정계수:', model.rvalue**2)# 0.7783127364499095
print('p-value:', model.pvalue)  # 2.8476895206683644e-50
print('표준오차:', model.stderr)   # 0.028577934409305443 ## 모델이 예측한 값과 실제값과의 차이
# y_hat = model.slope * x + model.intercept
print('점수예측 (IQ=80):', model.slope * 80 + model.intercept)
print('점수예측 (IQ=250):', model.slope * 156 + model.intercept)

print('점수예측:', np.polyval([model.slope, model.intercept], np.array(score_iq.iq))) # predict 대신
newdf = pd.DataFrame({'iq':[55, 66, 77, 88, 157]}) 
print('점수예측:', np.polyval([model.slope, model.intercept], newdf))