# 일원 분산 분석
# 어느 음식점의 매출 자료와 날씨 자료(온도를 세 그룹으로 분리)를 활용하여 온도에 따른 매출액의 평균에 차이가 있는 지 분석.


# 귀무 : 매출액은 온도에 영향이 없다.
# 대립 : 매출액은 온도에 영향이 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats

# 매출 자료 읽기.
sales_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv', dtype={'YMD':'object'})
print(sales_data.head(3))       # 1  20190519  18000    1
print(sales_data.info())


#날씨 자료
wt_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv')
print(wt_data.head(2))
print()

# sales_data 와 join 하기 위해 2018-06-01 => 20180601
wt_data.tm= wt_data.tm.map(lambda x:x.replace('-',''))
print(wt_data.head(2))

print()
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.head(5)) 

# 칼럼 추출
print(frame.columns)
data = frame.iloc[:, [0,1,7,8]]         # YMD, AMT, maxTa, sumRn
print(data.head(3))

print()
print(data.maxTa.describe())        # 일변 최고 온도에 대한 요약 통계량

# 시각화
# import matplotlib.pyplot as plt
# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 임의로 추움, 보통, 더움(0,1,2) 로 나눔.
data['ta_gubun'] = pd.cut(data.maxTa, bins =[-5, 8, 24, 37], labels=[0,1,2])
data = data[data.ta_gubun.notna()]
print(data.head(3), ' ', data.ta_gubun.unique())

# 등분산 검정, 정규성 검정 
x1 = np.array(data[data.ta_gubun == 0].AMT)
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)
print(stats.levene(x1,x2,x3).pvalue)        # 0.039002396565063324 < 0.05 이므로 등분산 만족 X

# 정규성 검정
print(stats.ks_2samp(x1, x2).pvalue)    # 9.28938415079017e-09
print(stats.ks_2samp(x1, x3).pvalue)    # 1.198570472122961e-28
print(stats.ks_2samp(x2, x3).pvalue)    # 1.4133139103478243e-13

# 온도별 매출액 평균
abc = data.loc[:, ['AMT', 'ta_gubun']]
print(abc.groupby('ta_gubun').mean())
print(pd.pivot_table(abc, index=['ta_gubun'], aggfunc='mean'))

print()
# ANOVA 분석
sp = np.array(abc)
group1 = sp[sp[:, 1] == 0, 0]
group2 = sp[sp[:, 1] ==1, 0]
group3 = sp[sp[:, 1] == 2, 0]

import matplotlib.pyplot as plt
# 시각화
# plt.boxplot([group1, group2, group3])
# plt.show()

print(stats.f_oneway(group1, group2, group3))   # F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
# p-value =2.360737101089604e-34 < 0.05        이므로 귀무가설 기각
print(stats.kruskal(group1,group2,group3))      # 정규성을 만족하지 못했으므로 kruskal-wallis test


# 등분산성을 만족하지 못했으므로Welch's ANOVA 를 수행
# Welch's ANOVA를 수행 하기 위한 pip package
# pip install pingouin
from pingouin import welch_anova
df = data
print(welch_anova(data=df, dv='AMT', between='ta_gubun'))
#      Source  ddof1     ddof2           F         p-unc       np2
# 0  ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038
# p-value = 7.907874e-35 < 0.05
# 해석 : 온도에 따른 어느 음식점의 매출액 차이가 유의미한 것으로 볼 수 있다.
# 그룹 간의 매출액의 차이를 확인 : 사후 검정이 필요

from statsmodels.stats.multicomp import pairwise_tukeyhsd
posthoc = pairwise_tukeyhsd(abc['AMT'], abc['ta_gubun'], alpha = 0.05)
print(posthoc)

fig = posthoc.plot_simultaneous()
plt.show()

# 각 그룹 간 매출액의 차이가 유의미 하다고 할 수 있다.
# 매출에 영향을 주는 요소는 온도 이외에도 많이 존재할 수 있으므로 
# 더 많은 독립변수들을 대상으로 결과를 파악해 보는 것이 중요하다.



