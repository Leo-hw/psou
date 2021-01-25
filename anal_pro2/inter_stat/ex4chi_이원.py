# 실습 : 교육 수준과 흡연율 간의 고나련성 분석: smoke.csv

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/smoke.csv')
print(data.head(3))
print(data['education'].unique())   #[1 2 3]
print(data['smoking'].unique())     #[1 2 3]

# 귀무 : 교육 수준과 흡연율 간에 관련이 없다. ( 독립이다.)
# 대립 : 교육 수준과 흡연율 간에 관련이 있다. (독립이 아니다.)
# 독립 : 범주형, 종속 : 범주형 <= 카이제곱 검정


#학력 수준별 흡연에 대한 교 차 표 작성.
ctab = pd.crosstab(index = data['education'], columns = data['smoking'])        # 빈도수 
#ctab = pd.crosstab(index = data['education'], columns = data['smoking'], normalize=True)        # 빈도 비율 
ctab.index=['대학원졸', '대졸', '고졸']
ctab.columns = ['과흡연','보통','비흡연']
print(ctab)

# 수식을 사용할 수 있으나 제공되는 메소드를 이용
chi_result = [ctab.loc['대학원졸'], ctab.loc['대졸'], ctab.loc['고졸']]
#chi2, p, ddof, expected = stats.chi2_contingency(chi_result)        # 이원 카이제곱.
chi2, p, ddof, expected = stats.chi2_contingency(ctab)      # 다른 컬럼이 없이 모든 컬림이 참여할 경우      
msg = 'chi2:{}, p-value:{}, df:{}'
print(msg.format(chi2, p, ddof))
print('expected : \n', expected)                
# 해석 :  p-value:0.0008182572832162924 < 알파 0.05 귀무가설 기각. 교육 수준과 흡연율 간에 관련이 있다.

# Yate 보정 : 분할표의 자유도가 1인 경우는 x^2값이 약간 높게 계산된다.
# 그래서 아래의 식과 같이 절대값 |0-E|에서 0.5를 뺀다음 제곱하며, 이 방법을 야트 보정이라 한다.

# 실습) 국가 전체와 지역에 대한 인종 간 인원 수로 독립성 검정 실습
#두 집단 ( 국가 전체 - national, 특정지역 - la) 의 인종 간 인원 수의 분포가 관련이 있는가?
# 귀무 : 국가 전체와 특정지역의 인종간 인원수의 분포가 관련이 없다.
# 대립 : 국가 전체와 특정지역의 인종간 인원수의 분포가 관련이 있다.
national = pd.DataFrame(['white']*100000 + ['hispanic']* 60000 + ['black']*50000 +['asian']*15000 +['other']*35000)
la = pd.DataFrame(['white']*600 + ['hispanic']* 300 + ['black']*250 +['asian']*75 +['other']*150)

print(national)
print(la)
na_table = pd.crosstab(index=national[0], columns='count')
la_table = pd.crosstab(index=la[0], columns='count')
na_table['count_la'] = la_table['count']
print(na_table)

chi2, p, df, _ = stats.chi2_contingency(na_table)
print('chi2: ', chi2, ', p-value:', p, ' , df: ', df)
# p-value: 0.0011800326671747886  < 0.05 이므로 귀무가설을 기각. 국가 전체와 특정 지역의 인종 간 인원의 관련이 없다.
