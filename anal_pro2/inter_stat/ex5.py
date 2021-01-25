'''
동질성 검정 - 두집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 두 집단 이상에서 각범주(집단) 간의 비율이 서로
동일한가를 검정하게 된다. 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.
동질성 검정 실습1) 교육방법에 따른 교육생들의 만족도 분석 - 동질성 검정 survey_method.csv

https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/survey_method.csv
'''
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/survey_method.csv")
print(data.head())
print(len(data)) # 150
print(data['method'].unique()) # [1 2 3]

# 귀무 : 교육 방법에 따른 교육생들의 만족도에 차이가 없다.
# 대립 : 교육 방법에 따른 교육생들의 만족도에 차이가 있다.

ctab = pd.crosstab(index = data['method'], columns=data['survey'])
ctab.columns = ['매우만족','만족','보통','불만족','매우불만족']
ctab.index = ['방법1','방법2','방법3']
print(ctab)

chi2, p, _, _ = stats.chi2_contingency(ctab)
print('chi2 : ', chi2, ', p_value :', p)
# 해석 : p_value : 0.5864574374550608 > 0.05 이므로 귀무 가설 채택. 교육방법에 따른교육생들의 만족도에 차이가 없다.

print('***'* 20)
# 동질성 검정 실습2) 연령대별 sns 이용률의 동질성 검정
# 20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 SNS 서비스들에 대해 이용 현황을 조사한 자료를 바탕으로 연령대별로 홍보
# 전략을 세우고자 한다.
# 연령대별로 이용 현황이 서로 동일한지 검정해 보도록 하자.
sns_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/snsbyage.csv")
print(sns_data)
print(sns_data['age'].unique()) # [1 2 3]
print(sns_data['service'].unique()) # ['F' 'T' 'K' 'C' 'E']

# 귀무 : 연령대별로 SNS서비스 들에 대한 이용 현황은 동일하다.
# 대립 : 연령대별로 SNS서비스 들에 대한 이용 현황은 동일하지않다..

ctab2 = pd.crosstab(index = sns_data['age'], columns = sns_data['service']) # 나이대별 서비스 선정 인원수
print(ctab2)
chi2, p, df, exp = stats.chi2_contingency(ctab2)
print('chi2 : ', chi2, ', p : ', p, ', df', df)

# 해석 : p :  1.1679064204212775e-18 < 0.05 이므로 귀무가설 기각
# 연령대별로 SNS 서비스들에 대해 이용 현황은 동일하지 않다.