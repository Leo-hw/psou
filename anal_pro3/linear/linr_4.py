# 단순 선형 회귀 분석을 통해 결정계수, p-value, t-value, f-value

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/drinking_water.csv')
print(df.head(2))
print(df.corr())

import statsmodels.formula.api as smf
model = smf.ols(formula = '만족도~ 적절성', data = df).fit()
print(model.summary())
