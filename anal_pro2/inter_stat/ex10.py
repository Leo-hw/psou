# 일원 분산으로 집단 간의 평균 차이 검정.

import scipy.stats as stats
import pandas as pd
import numpy as np
import urllib.request
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt'

data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
print(data)

# 강남구 소재 gs 편의점 알바생의 3개 지역 급여에 대한 평균 차이를 검정하시오
# 귀무 :  3개 지역 급여에 대한 평균에 차이가 없다.
# 대립 :  3개 지역 급여에 대한 평균에 차이가 있다.


gr1 = data[data[:, 1]== 1, 0]
gr2 = data[data[:, 1]== 2, 0]
gr3 = data[data[:, 1]== 3, 0]
print(gr1)
print(gr2)
print(gr3)
print(np.average(gr1), ' ', np.average(gr2), ' ', np.average(gr3))      # 316.625   256.44444444444446   278.0

print(stats.shapiro(gr1))
print(stats.shapiro(gr2))
print(stats.shapiro(gr3))

# 시각화
# plot_data = [gr1, gr2, gr3]
# plt.boxplot(plot_data)
# plt.show()

#일원 분산 분석( one-way ANOVA)
f_statistic, p_val = stats.f_oneway(gr1, gr2, gr3)
print('f_statistic :', f_statistic, ', p_val : ', p_val)
# p_val :  0.043589334959178244 < 0.05  이므로 귀무가설 기각

print()
# 일원 분산 분석2 : linear model 을 이용
df = pd.DataFrame(data, columns=['value', 'group'])
#print(df)

model = ols('value ~ C(group)', df).fit()
print(anova_lm(model))
