# DB의 자료를 읽어 가설 검정 정리

import MySQLdb
import pandas as pd
import numpy as np
import ast
import scipy.stats as stats

with open('mariadb.txt', 'r') as f:
    config = f.read()
    
config = ast.literal_eval(config)
#print(config)

# RemoteDB : MariaDB 와 연동
conn = MySQLdb.connect(**config)
cursor = conn.cursor()

sql = """
select jikwon_no, jikwon_name, jikwon_jik, jikwon_pay from jikwon where jikwon_jik = '과장'
"""

cursor.execute(sql)

for data in cursor.fetchall():
    print('%s%s%s%s'%data)
    
print('\n -- 교차 분석 (이원 카이 제곱 : 독립변수 - 범주형, 종속변수- 범주형)')
df = pd.read_sql("select * from jikwon", conn)
print(df.head(3), ' ', df.shape)

print()
print('각 부서와 직원평가점수 간의 관련성 여부 분석')
# 귀무 : 부서와 평가점수는 관련이 없다.
# 대립 : 부서와 평가점수는 관련이 있다.
buser = df['buser_num']
rating = df['jikwon_rating']
ctab = pd.crosstab(buser, rating)       # 교차표 작성(이원 카이제곱)
print(ctab)

chi, p, ddof, expected = stats.chi2_contingency(ctab)
print("chi:{}, p:{}, df:{}".format(chi, p, ddof))
# chi:7.339285714285714, p:0.2906064076671985, df:6
# 유의수준 0.05
# 해석1 : p-value : 0.2906064076671985 > 0.05    귀무가설 채택.
# 해석2: 임계치 12.592  chi:7.339285714285714 값이 c.v(임계치)의 왼쪽에 위치하므로, 귀무가설 채택. 

print('\n -- 차이 분석(t-test: 독립변수 - 범주형, 종속변수 - 연속형)')
print('10, 20번 부서간 연봉 평균 값의 차이 여부를 검정하시오.')
# 귀무 : 두 부서간 연봉에 차이가 없다. 
# 대립 : 두 부서간 연봉에 차이가 있다.
df_10 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num = 10", conn)
df_20 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num = 20", conn)
buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']
print(np.mean(buser10), ' ', np.mean(buser20))
t_result = stats.ttest_ind(buser10, buser20)
print(t_result)
#Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
# 해석 : pvalue=0.6523879191675446 > 0.05 이므로 귀무가설 채택. 두 부서간 연봉에 차이가 없다.

print('\n -- 분산 분석(ANOVA: 독립변수 - 범주형, 종속변수 - 연속형)')
from statsmodels.formula.api import ols
import statsmodels.api as sm
import matplotlib.pyplot as plt

print('각 부서 (Factor : 부서, 10,20,30,40: Factor level)의 평균값의 차이를 검정')
# 귀무 : 각 부서 사이에 연봉 평균에 차이가 없다.
# 대립 : 각 부서 사이에 연봉 평균에 차이가 있다.
df3 = pd.read_sql("select * from jikwon", conn)
print(df3.head(2))
buser = df3['buser_num']     # 범주형 (명목척도)
pay = df3['jikwon_pay']        # 연속형 (비율척도)

group1 = df3[df3['buser_num'] == 10] ['jikwon_pay']
group2 = df3[df3['buser_num'] == 20] ['jikwon_pay']
group3 = df3[df3['buser_num'] == 30] ['jikwon_pay']
group4 = df3[df3['buser_num'] == 40] ['jikwon_pay']
# print(group1)
# print(group2)

# 시각화
# plot_data = [group1,group2,group3,group4 ]
# plt.boxplot(plot_data)
# plt.show()

f_sta, p_val = stats.f_oneway(group1,group2,group3,group4)
print('부서별 직원 연봉 평균 차이 검정 결과 : f={0:.5f}, p={1:,.5f}'.format(f_sta, p_val))
# p=0.74544 > 0.05 이므로 귀무 채택, 각 부서 사이에 연봉 평균에 차이가 없다.

print()
# 방법2 
lmodel = ols('jikwon_pay ~ C(buser_num)', data = df3).fit()
table = sm.stats.anova_lm(lmodel, type=2)
print(table)
# p=0.745442

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
result = pairwise_tukeyhsd(df3.jikwon_pay, df3.buser_num)
print(result)

result.plot_simultaneous()
plt.show()
