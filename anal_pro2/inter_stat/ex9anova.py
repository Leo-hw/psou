#  ANOVA : 독립녀수(Factor - 여러 개의 Factor level로 구성)는 범주형, 종속변수: 연속형
# 여러 개의 Factor level(집단) 에 대한 평균 차이 검정. 분산분석, 변량분석
# f값 = Between Variable/ Within Variable
# 종속변수의 변화 폭이 우연 보다 필연에 위해 발생했는지 분석하는것
# 집단간 분산이 집단 내 분산보다 충분히 큰 것인가를 파악.
# 선행 조건: 독립성, 정규성, 등분산성

# * 서로 독립인 세 집단의 평균 차이 검정
# 실습) 세가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/three_sample.csv')
print(data.head(3), len(data))  #80

# 교육방법(독립변수 - Factor: 1개, Factor level: 3개 - 범주형), 시험점수의 차이 < - 종속변수 : 연속형 데이터 
# 일원 분산 분석 (one-way ANOVA)
# 귀무 : 세가지 교육방법을 적용하여 시험을 실시한 결과 점수에 차이가 없다. 
# 대립: 세가지 교육방법을 적용하여 시험을 실시한 결과 점수에 차이가 있다 . 
print(data.describe())  # 요약통계량으로 이상치를 확인함 

# 이상치(outlier) 확인을 위해 시각화
import matplotlib.pyplot as plt
#plt.boxplot(data.score)
#plt.hist(data.score)
#plt.show()

data = data.query('score <= 100')
print(data.describe())
print(len(data))   # 78

# 등분산성 확인 - 만족하면 anova, 만족안하면 welch_anova
result = data[['method','score']]
print(result.head(3))
m1 = result[result['method']==1]
m2 = result[result['method']==2]
m3 = result[result['method']==3]
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print('등분산 확인:', stats.levene(score1, score2, score3).pvalue) #0.1132>0.05 만족 합니다    레베네 제일 많이 쓴다 
print('등분산 확인:', stats.fligner(score1, score2, score3).pvalue) #  0.10847 > 0.05 만족합니다
print('등분산 확인:', stats.bartlett(score1, score2, score3).pvalue)

#정규성 확인 - 만족하면 anova, 만족 안하면 kruscal-wallis test
#집단 하나에 검정
print(stats.shapiro(score1))
print(stats.shapiro(score2))
print(stats.shapiro(score3))
# 여러 개 검정
print('정규성 확인:', stats.ks_2samp(score1, score2))
print('정규성 확인:', stats.ks_2samp(score1, score3))
print('정규성 확인:', stats.ks_2samp(score2, score3))   #보다시피 정규성 에서 모든 학목에서 0.05 보다 커서 정규성을 만족시킨다 
# 하지만 모든 항목에서 정규성을 만족 못하면 그래도 정규성 만족 한다고 봐야한다

print()
# 교차표 : 교육방법별 건수 
# data2 = pd.crosstab(index = data['method'], column = 'count')
# data2.index = ['방법1','방법2','방법3']
# print(data2)

# 교차표 : 교육방법별 만족여부 
data3 = pd.crosstab(data.method, data.survey)
data3.index = ['방법1','방법2','방법3']
data3.columns = ['만족','불만족']
print(data3)
print('\nANOVA 검정 - linear model 을 사용')
import statsmodels.api as sm
# regModel = ols('data["score"] ~ data["method"]', data=data).fit()   # 단순회귀 모델 생성
regModel = ols('data["score"] ~ C(data["method"])', data=data).fit() # 해당컬럼이 범주형임을 명시적 기술
print(regModel)

table = sm.stats.anova_lm(regModel, type=1)  #typ =1, typ =2, typ=3
print(table)  # 유위확률 p : 0.939639 > 0.05 귀무 채택. 세가지 교육방법을 적용하여 시험을 실시한 결과 점수 

'''
# 참고 : 다중회귀 모델로ANOVA 검정 
regModel2 = ols('data["score"] ~ C(data.method+ data["survey"])', data = data).fit()
table2 = sm.stats.anova_lm(regModel2, type=1)
print(table2)
'''

# 사후 검정 : ANOVA는 전체에 대한 평균의 차이여부만 알려줍니다 
# 각 그룹 간의 차이를 알고자 한다면 Post Hoc Test를 하게 된다.
from statsmodels.stats.multicomp import pairwise_tukeyhsd

turkeyResult = pairwise_tukeyhsd(data.score, data.method)
print(turkeyResult)   #reject 가 False 면 평균 차이가 없다 

#시각화 
turkeyResult.plot_simultaneous()
plt.show()
