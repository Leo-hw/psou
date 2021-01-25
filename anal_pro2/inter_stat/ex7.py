# 두 집단의 가설검정 - 실습 시 분산을 알지 못하는 것으로 한정하겠다

import pandas as pd
from scipy import stats
from numpy import average


# 실습 1) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
# 서로 독립인 두 집단의 평균 차이 검정 (independent samples t test)
# 남녀의 성적 A 반과 B 반의 키 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을
# 독립표본 (two sample) 이라고 한다
male = [75, 85, 100, 72, 86]
female = [63, 76, 52, 100, 70]

# t-test를 위한 통계적 질문 : 남녀의 시험 평균이 우연히 같을 확률은?

print('male:', average(male)) # 83.6
print('female:', average(female)) # 72.2

# 11.4점 차이가 나는 평균 차이가 우연히 발생할 확률은 얼마나 되는가?

# 귀무 가설: 두 집단 간 파이썬 시험의 평균에 차이가 없다.
# 대립 가설: 두 집단 간 파이썬 시험의 평균에 차이가 있다.

# 선행 조건: ① 정규성을 띄어야 되며, ② 등분산성을 만족시켜야 된다.
two_sample = stats.ttest_ind(male, female)
two_sample = stats.ttest_ind(male, female, equal_var = True) # (default) 정규분포의 분산을 같다.
# stats.ttest_1samp(): T-test for the mean of ONE group (집단이 하나일 때)
# stats.ttest_ind(): T-test for the mean of ONE group (집단이 두개일 때)
print(two_sample) # Ttest_indResult(statistic=1.2118063278722324, pvalue=0.26016072398920453)
# 해석: p (0.260) > α (0.05) → 귀무가설 채택 (평균 차이가 우연히 발생한 것, 평균은 원래 차이가 없다.)


# 실습 2) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행
data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/two_sample.csv')
print(data.head())
ms = data[['method','score']]
print(ms.head())
print(ms.method.unique()) # [1 2]

# 귀무 가설: 두 가지 교육 방법에 따른 평균 시험 점수에 차이가 없다.
# 대립 가설: 두 가지 교육 방법에 따른 평균 시험 점수에 차이가 있다.

m1 = ms[ms.method == 1]
m2 = ms[ms.method == 2]
# print(m1.head())
# print(m2.head())

score1 = m1['score']
score2 = m2['score'] # NaN 포함
print(score1)
print(score2)

# NaN 확인
print(score1.isnull().sum())
print(score2.isnull().sum()) # True(NaN)를 1로써 총 개수를 구할 수 있음

# NaN 처리 (제거 / 0 치환 / ...)
## ① NaN을 0으로 처리
# sco1 = score1.fillna(0) 
# sco2 = score2.fillna(0) 
## ② NaN을 평균값으로 처리
sco1 = score1.fillna(score1.mean()) 
sco2 = score2.fillna(score2.mean())
## ③ 제거 (dropna)

# 정규성 확인 (p-value > 0.05 인가?)
print('sco1 정규성:', stats.shapiro(sco1))
# ShapiroResult(statistic=0.965552806854248, pvalue=0.3679903745651245) p > 0.05 (정규성 만족)
print('sco2 정규성:', stats.shapiro(sco2))
# ShapiroResult(statistic=0.9621098637580872, pvalue=0.6714189648628235) p > 0.05 (정규성 만족)

# 등분산성 확인 (p-value > 0.05인가?
print('등분산성(levene)', stats.levene(sco1, sco2)) # 모수 검정 (가장 많이 쓰임)
# 등분산성(levene) LeveneResult(statistic=0.5626824030182838, pvalue=0.4568427112977609)
print('등분산성(fligner)', stats.fligner(sco1, sco2)) # 모수 검정
# 등분산성(fligner) FlignerResult(statistic=0.5878870391441374, pvalue=0.44323735267062647)
print('등분산성(bartlett)', stats.bartlett(sco1, sco2)) # # 비모수 검정
# 등분산성(bartlett) BartlettResult(statistic=1.2274825627365802, pvalue=0.26789717886602216)
## 모두 등분산성 만족 
## Tip! stats.levene(sco1, sco2).pvalue 하면 p-value만 출력 가능

print()
# 선행 조건을 모두 만족 시켰으니 t-test 진행
result = stats.ttest_ind(sco1, sco2) # (default) equal_var = True # 정규성, 등분산성을 만족시켰을 때
# result = stats.ttest_ind(sco1, sco2, equal_var = False) # 정규성 만족, 등분산성을 불만족시켰을 때
# print(stats.wilcoxon(sco1, sco2)) # 정규성 불만족 했을 때
print(result)
# Ttest_indResult(statistic=-0.19649386929539883, pvalue=0.8450532207209545)
# 해석: p (0.845) > α (0.05) → 귀무가설 채택
# 우연히 평균 차이가 났을 확률이 크다. 두 집단의 평균 점수 차이가 없다.
print(average(sco1), average(sco2))


