# 선형 회귀 분석: 독립변수 (연속형)가 종속변수(연속형)에 얼마나 영향을 주는 지 알아보기 위한 분석 방법
import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

# 방법1: model 없음
np.random.seed(1)
x, y, coef = make_regression(n_samples = 50, n_features = 1, bias = 100, coef = True)
# (default) bias = 0
print(x) # 독립 변수 (항상 2차원 배열임!)
print(y) # 종속 변수 (1차원 vector)
print(coef) # weight 회귀 계수 값 = 기울기 ## 90.34019152878835
# y = f(x) / y = b + wx / y = wx + b / y = coef * x + bias 
y_pred = coef * 50 + 100
print(y_pred) # 4617.009576439417
print()

print('-----------------')
# 방법2: model 있음
from sklearn.linear_model import LinearRegression

xx = x
yy = y

model = LinearRegression() # 내부적으로 최소 제곱 법을 사용하는 모델
print(model)
print(xx[0]) # -0.19183555
print(yy[0]) # 82.6695394576208
fit_model = model.fit(xx, yy) # (독립변수와 종속변수로 모형 추정하기 위해) 학습 시킴 → 최적의 기울기와 절편 등을 get  
print('기울기(회귀계수):', fit_model.coef_) # 90.34019153 (위에 모델 없이 구한 기울기 값과 같음)
print('절편:', fit_model.intercept_) # 100.0 (위 에서 bias = 100으로 정했기 때문)

# 잔차가 최소가 되는 추세선을 갖는 모델이 완성 (fit_model). 이 모델로 새로운 값을 예측할 수 있음
y_new = fit_model.predict(xx[[0]])
print(y_new) # 82.66953946

y_new = fit_model.predict([[50]])
print(y_new) # 4617.00957644
## 독립 변수가 1개 → 단순 회귀 

x_new, _, _ = make_regression(n_samples = 3, n_features = 1, bias = 100, coef = True)
print(x_new)
y_new = fit_model.predict(x_new)
print(y_new) # [164.8272023  106.39939598 191.27751443]
print()

print('-----------------')
# 방법3: ols() - model 있음
import statsmodels.formula.api as smf
import pandas as pd

x1 = xx.flatten() # 차원 축소 (2차원 → 1차원)
print(xx.shape, x1.shape)
y1 = yy
data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']
print(df.head())

model2 = smf.ols(formula = 'y1 ~ x1', data=df).fit() # (최소 제곱법 이용한) model형성
print(model2.summary()) # 기울기: 90.34 , 절편: 100
'''                         OLS Regression Results                            
==============================================================================
Dep. Variable:                     y1   R-squared:                       1.000 → 결정계수 (상관계수 제곱)
Model:                            OLS   Adj. R-squared:                  1.000 → 설명력
Method:                 Least Squares   F-statistic:                 1.249e+33
Date:                Wed, 25 Nov 2020   Prob (F-statistic):               0.00
Time:                        10:23:12   Log-Likelihood:                 1513.8
No. Observations:                  50   AIC:                            -3024.
Df Residuals:                      48   BIC:                            -3020.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975] → 기본 95% 신뢰구간
------------------------------------------------------------------------------
Intercept    100.0000   2.48e-15   4.03e+16      0.000     100.000     100.000 → 100 : 절편
x1            90.3402   2.56e-15   3.53e+16      0.000      90.340      90.340 → 90.34 : 기울기
==============================================================================
Omnibus:                        0.105   Durbin-Watson:                   0.479
Prob(Omnibus):                  0.949   Jarque-Bera (JB):                0.007
Skew:                           0.004   Prob(JB):                        0.996
Kurtosis:                       2.942   Cond. No.                         1.04
=============================================================================='''
# print(model2.predict()) # 50개 결과
print(model2.predict()[0])

# 새로운 값으로 예측하기 (DataFrame의 형식을 갖추는 게 좋음)
# print(x1[:2]) # [-0.19183555 -1.07296862]
x_new2 = pd.DataFrame({'x1':[-0.19, -1.07, 8, 88, 888]})
# print(x_new2)
y_new2 = model2.predict(x_new2)
print(y_new2)
'''
0       82.835364
1        3.335995
2      822.721532
3     8049.936855
4    80322.090078
'''

