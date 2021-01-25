# Two-way ANOVA : 독립변수(Factor) 복수 이고 독립변수당 그룹(Factor level) 이 복수, 범주형.
# https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt

import scipy.stats as stats
import pandas as pd
import numpy as np
import urllib.request
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt'

data = pd.read_csv(urllib.request.urlopen(url), delimiter=',')
#print(data)

# 상호작용은 빼고 처리
print()
reg = ols('data["머리둘레"] ~ C(data["태아수"]) + C(data["관측자수"])', data = data).fit()
table = anova_lm(reg, type=2)
print(table) 

print()
# 상호 작용이 있는 상태로 처리
formula = '머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)'
lmodel = ols(formula, data).fit()
print(anova_lm(lmodel))     
#해석  pvalue = 3.295509e-01 > 0.05 이므로 귀무가설 채택. 측정자와 태아수는 태아의 머리둘레 값에 연관성이 없다.
