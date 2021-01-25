# 회귀분석 문제 3) 
# 원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
# 장고로 작성한 웹에서 근무년수를 입력하면 예상연봉이 나올 수 있도록 프로그래밍 하시오.
import MySQLdb
import ast
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy import stats
plt.rc('font', family='malgun gothic')                        # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False           # 음수 부호 깨짐 방지

with open('mariadb.txt', 'r') as f:
    config = f.read()
    
config = ast.literal_eval(config)
#print(config)

# RemoteDB : MariaDB 와 연동
conn = MySQLdb.connect(**config)
cursor = conn.cursor()

sql = """
select jikwon_no, jikwon_name, jikwon_jik, year(now())-year(jikwon_ibsail) as jikwon_wday,jikwon_pay from jikwon
"""
    
df = pd.read_sql(sql, conn)

#df.rename(columns = {'jikwon_no' : '사번','jikwon_name':'직원명','jikwon_jik':'직급','jikwon_wday':'근무년수','jikwon_pay':'연봉'}, inplace = True)
print(df.head(3), ' ', df.shape)

# 상관 관계 확인
#print(df.loc[:, ['근무년수','연봉']].corr())
print(df.loc[:, ['jikwon_wday','jikwon_pay']].corr())

# ols() 사용하여 선형 회귀 모델
#lm = smf.ols(formula = '근무년수 ~ 연봉', data = df).fit()
lm = smf.ols(formula = 'jikwon_pay ~ jikwon_wday', data = df).fit()
print(lm.summary())
'''
# 시각화
plt.scatter(df['근무년수'], df['연봉'])
plt.xlabel("근무년수")
plt.ylabel("연봉")
plt.show()
'''
print(lm.summary().tables[1])
# 예측 : predict()
# x_new = pd.DataFrame({'jikwon_wday':[10,15,]})
# print(lm.predict(x_new))

# 값을 입력받아 처리
ndf = float(input('근무 년수를 입력하세요'))
x_new = pd.DataFrame({'jikwon_wday':[ndf]})
print(lm.predict(x_new))

# 잔차의 독립성
# Duirbin-Watson : 1.572

print()
# 2) 모형의 선형성 확인 : 예측값과 잔차의 비교 
fitted = lm.predict(df)
residual = df['jikwon_pay'] - fitted
sns.regplot(fitted, residual, lowess = True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color = 'blue')
plt.show()
# 많이 벗어나는 거 같은데?

# 2) 잔차의 정규성 확인
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

import statsmodels.api as sm
sm.graphics.influence_plot(lm, alpha = 0.05, criterion='cooks')
plt.show()
