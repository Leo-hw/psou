# 선형회귀방법4 - linregress() : 모델 있음

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# iq 에 따른 시험 점수 값 예측
score_iq = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/score_iq.csv')
print(score_iq.head(3))
print(score_iq.info())

x = score_iq.iq
y = score_iq.score

# 상관 관계 확인
print(np.corrcoef(x,y))
print(score_iq.corr())

# plt.scatter(x, y)
# plt.show()

# iq와 score 에 영향을 준다고 가정 - 인과관계가 있으므로 회귀분석이 가능
model = stats.linregress(x, y)
print(model)
print('기울기 : ', model.slope)
print('절편 : ', model.intercept)
print('상관계수 : ', model.rvalue)
print('결정계수 : ', model.rvalue**2)
print('p-value : ', model.pvalue)
print('표준오차 : ', model.stderr)
# y_hat = model.slope * x + model.intercept
print('점수예측 : ', model.slope * 80 + model.intercept)
print('점수예측 : ', model.slope * 157 + model.intercept)
from scipy import polyval
#print('점수 예측 : ', np.polyval([model.slope, model.intercept], np.array(score_iq['iq']))
newdf = pd.DataFrame({'iq':[55,66,77,88,157]})

print(np.polyval([model.slope, model.intercept], newdf))