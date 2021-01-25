# 단순 선형 회귀 분석을 통해  상관계수[r], 결정계수[r^2], p-value, t-value, f-value 등을 이해하기
# 귀납적, 결정론적 방법
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/drinking_water.csv')
print(df.head())
print(df.corr()) # (default) method = 'pearson'
'''       친밀도       적절성       만족도
친밀도  1.000000  0.499209  0.467145
적절성  0.499209  1.000000  0.766853
만족도  0.467145  0.766853  1.000000'''

import statsmodels.formula.api as smf

model = smf.ols(formula = '만족도 ~ 적절성', data = df).fit() # 종속 변수 ~ 독립 변수 순 ## 연속형 데이터
print(model.summary())
'''                         OLS Regression Results                        ↓ 1에 가까울 수록 완벽 (BUT 현실성 없음, 기형적 모델 취급)    
============================================================================== # 학습 모델 뿐 아니라 새로 입력한 값에 대해서도 잘 예측해야 좋은 모델
Dep. Variable:                    만족도   R-squared:                       0.588 → 설명력[결정계수]: 얼마나 잘 예측해주느냐 지표
Model:                            OLS   Adj. R-squared:                  0.586 → r-squared와 크게 차이나면 독립변수 이상한 것
Method:                 Least Squares   F-statistic:                     374.0 → f = t^2
Date:                Wed, 25 Nov 2020   Prob (F-statistic):           2.24e-52 → < 0.05 (유의한 통계 자료임) (based on f)
Time:                        12:26:55   Log-Likelihood:                -207.44    이 모델로 예측한 값은 어느정도 신뢰가 있다.
No. Observations:                 264   AIC:                             418.9
Df Residuals:                     262   BIC:                             426.0
Df Model:                           1               ↑ 모델 전체에 대한p-value                          
Covariance Type:            nonrobust               ↓ 모델 각 각에 대한 p-value (<0.05 이므로 의미있는 통계임)            
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975] → coef 값 계수 들이 (신뢰 구간 95%)범위 내에 있음
------------------------------------------------------------------------------
Intercept      0.7789      0.124      6.273      0.000       0.534       1.023 → t = coef / std err
적절성            0.7393(b)   0.038     19.340      0.000       0.664       0.815     → b: 회귀 계수 (영향력의 세기) [우연일 가능성이 낮음]
==============================================================================   std err: 작을 수록 좋다 (회귀계수랑 반비례)
Omnibus:                       11.674   Durbin-Watson:                   2.185
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
Skew:                          -0.328   Prob(JB):                     0.000335
Kurtosis:                       4.012   Cond. No.                         13.4
=============================================================================='''
print('파라미터[절편[:', model.params) # 0.778858
print('결정계수:', model.rsquared) # 0.5880630629464404
print('p값:', model.pvalues) # 1.454388e-09
print('실제값:', df.만족도[0], ', 모델이 예측한 값:', model.predict()[0]) # 3, 3.7359630488589186

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1) # R의 abline
plt.plot(df.적절성, df.적절성 * slope + intercept, 'b')
plt.show()