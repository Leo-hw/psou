# 광고 매체를 통한 광고비 증가로 판매량을 예측하기 위한 선형 회귀모델

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import statsmodels.formula.api as smf


advdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv', 
                          usecols=[1,2,3,4])
print(advdf.head())
print(advdf.shape)
print(advdf.index, advdf.columns)
print(advdf.info())

# 상관 관계 확인
print(advdf.loc[:, ['sales','tv']].corr())

# ols() 사용하여 선형 회귀 모델
lm = smf.ols(formula = 'sales ~ tv', data = advdf).fit()
print(lm.summary())

'''
# sales 와 tv 자료로 시각화 
plt.scatter(advdf.tv, advdf.sales)
plt.xlabel("tv(in 1000's)")
plt.ylabel("sales(in 1000's)")
x = pd.DataFrame({'tv':[advdf.tv.min(), advdf.tv.max()]})
y_pred = lm.predict(x)
plt.plot(x, y_pred, c='red')
plt.title('Simple Linear Regression')
plt.show()
'''
print(lm.summary().tables[1])
# 예측 : predict()
x_new = pd.DataFrame({'tv':[100]})
print('tv 광고비에 대한 판매 예측값 : ', lm.predict(x_new))

print()
x_new = pd.DataFrame({'tv':[110, 500, 1500]})
print('tv 광고비에 대한 판매 예측값 : ', lm.predict(x_new))

print('--------------------------')
# ols() 사용하여 다중 선형 회귀 모델
lm_mul = smf.ols(formula = 'sales ~ tv + radio + newspaper', data = advdf).fit()
print(lm_mul.summary())
print(advdf.corr())

print('\n 선형회귀 모델 만족 조건 ----')
# 1) 잔차의 독립성 확인 : Durbin-Watson 통계량을 사용하여 회귀 모형의 오차에 자기 상관이 있는지 검정할 수 있습니다.
#                                         자기 상관은 인접 관측치의 오차가 상관되어 있음을 의미합니다.
# Durbin -Watson 방법으로 확인 : 0~4 까지의 값을 가짐.    0 에 근사하면 양의 상관관계, 4에 근사하면 음의 상관관계
# 2에 근사하면 자기 상관이 없다. 다시말해 잔차끼리 상관관계를 가지지 않는다.
# Durbin-Watson : 2.084

print()
# 2)  모형의 선형성 확인 : 예측값과 잔차의 비교 ( 비슷하게 나와야 함)
import seaborn as sns
fitted = lm.predict(advdf)
residual = advdf['sales'] - fitted
sns.regplot(fitted, residual, lowess = True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color='blue')
plt.show()      # 빨간 실선이 파선을 크게 벗어나지 않으므로, 선형성 만족.

# 2)  잔차의 정규성 확인 : 잔차가 정규분포를 따라야 함.
# Q-Q plot 으로 확인.
import scipy.stats
sr = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x,y)
plt.plot([-3,3], [-3,3], '--', color='grey')
plt.show()

# 3) 잔차의 등 분산성 확인 : 회귀 모형을 통해 예측값들 대소에 관계 없이,  모든 값들에 대해 잔차의 분산이 동일해야 한다는 가정
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws={'color':'red'})
plt.show()

print()
# 4) 잔차의 등분산성 확인 : Cook's distance 는 극단값을 나타내는 지표
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm).cooks_distance
print(cd.sort_values(ascending=False).head())
print(advdf.iloc[[35,178,25,175,131]])

import statsmodels.api as sm
sm.graphics.influence_plot(lm, alpha = 0.05, criterion='cooks')
plt.show()