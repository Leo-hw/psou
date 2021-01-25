# iris dataset으로 선형 회귀 분석
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

iris = sns.load_dataset('iris')
print(iris.head(2))

# sns.pairplot(iris, hue = 'species', height=1.5)
# plt.show()
print()

# 변수 간 상관 관계
print(iris.corr())
'''              sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000    -0.117570    # 0.871754     0.817941
sepal_width      -0.117570     1.000000     -0.428440    -0.366126
petal_length      0.871754    -0.428440      1.000000     0.962865
petal_width       0.817941    -0.366126      0.962865     1.000000'''
print()

# 회귀 모델 : 상관관계가 약한 변수를 사용
result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()
# print('result1 요약 결과표\n', result1.summary())
'''                          OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared:                       0.014 → 너무 약한 상관관계 
Model:                            OLS   Adj. R-squared:                  0.007
Method:                 Least Squares   F-statistic:                     2.074
Date:                Wed, 25 Nov 2020   Prob (F-statistic):              0.152 > 0.05 → 유효하지 않은 통계값
Time:                        15:19:23   Log-Likelihood:                -183.00
No. Observations:                 150   AIC:                             370.0
Df Residuals:                     148   BIC:                             376.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept       6.5262      0.479     13.628      0.000       5.580       7.473
sepal_width    -0.2234      0.155     -1.440      0.152      -0.530       0.083
==============================================================================
Omnibus:                        4.389   Durbin-Watson:                   0.952
Prob(Omnibus):                  0.111   Jarque-Bera (JB):                4.237
Skew:                           0.360   Prob(JB):                        0.120
Kurtosis:                       2.600   Cond. No.                         24.2
=============================================================================='''
# print('result1 R-squared', result1.rsquared) # 0.013822654141080859
# print('result1 p-value', result1.pvalues) # 6.469702e-28




result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()
print('result2 요약 결과표\n', result2.summary())
'''                          OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared:                       0.760 → 강한 상관 관계!
Model:                            OLS   Adj. R-squared:                  0.758
Method:                 Least Squares   F-statistic:                     468.6
Date:                Wed, 25 Nov 2020   Prob (F-statistic):           1.04e-47 < 0.05 → 유의미한 통계
Time:                        15:24:48   Log-Likelihood:                -77.020
No. Observations:                 150   AIC:                             158.0
Df Residuals:                     148   BIC:                             164.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        4.3066      0.078     54.939      0.000       4.152       4.462
petal_length     0.4089      0.019     21.646      0.000       0.372       0.446
==============================================================================
Omnibus:                        0.207   Durbin-Watson:                   1.867
Prob(Omnibus):                  0.902   Jarque-Bera (JB):                0.346
Skew:                           0.069   Prob(JB):                        0.841
Kurtosis:                       2.809   Cond. No.                         10.3
=============================================================================='''
pred = result2.predict()
# print(pred) # 모든 데이터에 대한 예측값
print('예측값:', pred[:5]) # 4.879094603339241
print('실제값:', iris.sepal_length[:5]) # 5.1

# 새로운 data 예측
new_data = pd.DataFrame({'petal_length':[1.4, 0.8, 8.0]})
y_pred_new = result2.predict(new_data)
print('새로운 data로 예측한 sepal_length 결과:\n', y_pred_new)
print()

print('\n다중회귀분석: 독립변수 복수개') # 'y ~ x1 + x2 + x3 ....'
result3 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width', data = iris).fit()
print('result3 요약 결과표\n', result3.summary())
'''                          OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared:                       0.766 → 설명력이 높다
Model:                            OLS   Adj. R-squared:                  0.763
Method:                 Least Squares   F-statistic:                     241.0
Date:                Wed, 25 Nov 2020   Prob (F-statistic):           4.00e-47 < 0.05 (유의한 통계)
Time:                        15:40:43   Log-Likelihood:                -75.023
No. Observations:                 150   AIC:                             156.0
Df Residuals:                     147   BIC:                             165.1
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        4.1906      0.097     43.181      0.000       3.999       4.382
petal_length     0.5418      0.069      7.820      0.000       0.405       0.679 → P < 0.05 (유의함)
petal_width     -0.3196      0.160     -1.992      0.048      -0.637      -0.002 → P < 0.05 (유의함)
==============================================================================
Omnibus:                        0.383   Durbin-Watson:                   1.826
Prob(Omnibus):                  0.826   Jarque-Bera (JB):                0.540
Skew:                           0.060   Prob(JB):                        0.763
Kurtosis:                       2.732   Cond. No.                         25.3
=============================================================================='''
print('result3 R-squared', result3.rsquared)
print('result3 p-value', result3.pvalues)

## 참고: 여러개의 독립 변수를 더 효율적으로 비교하고 싶을 때 
## result3 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width', data = iris).fit()

## column_select = "+".join(iris.columns.difference('sepal_with','sepal_length','species'))
## difference(): 칼럼 중 제외할 칼럼 빼고 나머지
## formula = 'sepal_length ~' + column_select
## result3 = smf.ols(formula =formula, data=iris).fit()

# 새로운 data 예측
new_data2 = pd.DataFrame({'petal_length':[1.4, 0.8, 8.0], 'petal_width':[0.2, 0.8, 1.5]})
y_pred_new2 = result2.predict(new_data2)
print('새로운 data로 예측한 sepal_length 결과:\n', y_pred_new2)
print()


# 다중공선성(Multicollinearity)과 VIF(Variance Inflation Factors)
# 다중회귀모형에서 일부 독립변수가 다른 독립변수와 상관관계가 너무 높은 경우 문제 발생

# VIF > 10 인 경우 다중공선성 발생. 변수 선택에 신중해야 함.

# 다중 공선성 확인 방법
from statsmodels.stats.outliers_influence import variance_inflation_factor
del iris['species'] # 삭제 시에는 iris.species X
# print(iris.columns)
vifDf = pd.DataFrame()
vifDf['features'] = iris.columns
vifDf['vif_factor'] = [variance_inflation_factor(iris.values, i) for i in range(iris.shape[1])]
# 생성 시에도 vifDf.vif_factor X
print(vifDf) # 모든 값이 10을 넘는다. (다중 공선성 발생)