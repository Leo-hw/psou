# 이항분포 : 이항 검정 - 결과가 두 가지 값을 가지는 경우 확률 변수의 분포를 판단하는데 효과적
# 이산변량 사용
import pandas as pd
import scipy.stats as stats

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/one_sample.csv')
ctab = pd.crosstab(index=data['survey'], columns='count')
ctab.index = ['불만족', '만족']
print(ctab)     # 직원 대상으로 고객대응 교육에 대한 고객안내 서비스 만족여부 교차 분할표

# 귀무 : 직원 대상으로 고객대응 교육 후 고객 안내 서비스 만족도는 80%이다.
# 대립 : 직원 대상으로 고객대응 교육 후 고객 안내 서비스 만족도는 80%가 아니다.

# 양측 검정 : 기존 80% 기준 검증 실시
#stats.binom_test(성공 또는 실패 횟수, n=시도 횟수, p=가설확률, alternative='검정방법')
x = stats.binom_test([136, 14], p=0.8, alternative='two-sided')
print(x)        # p-value : 0.0006734701362867019 < 0.05
# 해석 : 귀무가설을 기각, 기존 80% 와 차이가 있다.        기존 만족률보다 크다, 작다라는 방향성을 제시하지 않는다.

print()
# 양측 검정 : 기존 20% 불만족률 기준 검증 실시
x = stats.binom_test([14, 136], p=0.2, alternative='two-sided')
print(x)        #p-value :0.000673470136286707 < 0.05


print('\n 단측 검정 : 방향성을 갖는다. 크다, 작다')
# 만족률이 클거라 가정하고, alternative = 'greater'
x = stats.binom_test([136, 14], p=0.8, alternative='greater')
print(x)
# 해석 : p-value: 0.0003179401921985477 < 0.05 귀무가설을 기각, 기존 만족률 80% 이상의 효과를 볼 수 있다.

print()
# 만족률이 작을거라 가정하고, alternative = 'less'
x = stats.binom_test([14, 136], p=0.2, alternative='less')
print(x)
# 위와 같은 값.


