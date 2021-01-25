# 가설 검정 중 교차 분석(Chi2) - 독립변수: 범주형, 종속 변수: 범주형
# 검정통계량 Chi2  = ( 관측값 - 기대값) **2 의 합/ 기대값

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/pass_cross.csv', encoding='euc-kr')

print(data.head())      # 표본 추출된 데이터(복원)
print(data.shape)       # (50, 4)

# 귀무 : 벼락치기 공부는 합격 여부와 관련이 없다.    # =, 0이 기본 개념
# 대립 : 벼락치기 공부는 합격 여부와 관련이 있다.    # 
# 가설 검정 실시            # 공부함:1, 합격:1

print(data[(data['공부함'] == 1) & (data['합격'] == 1)].shape[0])        # 18
print(data[(data['공부함'] == 1) & (data['불합격'] == 1)].shape[0])    # 7

# 빈도표
print('\n----- 빈도표 -----\n')

data2 = pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True)
data2.columns=['합격', '불합격','행합']
data2.index=['공부함','공부안함','열합']
print(data2)

# 기대도수 = ( 각 행의 주변 합) * (각 열의 주변 합)
print(25 * 30/50)
print(25 * 20/50)

'''
기대값
                합격  불합격  행합
공부함      15    10        25
공부안함  15   10      25
열합         30   20      50
'''

chi2 = (18-15)**2/ 15+(7-10)**2/10 + (12-15)**2/15 + (13-10)**2/10
print('chi2 : ' , chi2) # 3.0

#  자유도 : (행의 갯수 -1) * (열의 갯수 -1)
# df : 1
# 95 % 신뢰 구간에서 유의 수준(알파) 0.05
# 카이 제곱표를 통해 임계치 얻기 : 3.84
# 결론 : chi2 < 임계치 이므로 귀무 채택역 내에 존재함, 귀무가설을 채택.


#python 이 제공하는 모듈을 사용하여 가설 검증
import scipy.stats as stats
chi, p, _, _ = stats.chi2_contingency(data2)
print('chi : ' , chi, ' p-value : ' ,p)

# 결론 : 유의 수준 = 0.05 < p-value = 0.5578 이므로 귀무가설을 채택.

# 목적 : 두 범주형 변수 간에 독립성 검정, 적합도 검정, 동질성 검정