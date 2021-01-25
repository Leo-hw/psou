# 상관관계 분석

import pandas as pd
import numpy as np

"""
df = pd.DataFrame({'id1':(1,2,3,4,5), 'id2':(2,3,-1,7,9)})
print(df)
plt.scatter(df.id1, df.id2)
plt.show()

print(df.cov()) # 공분산 : 관계를 표현하기에 수치가 일정하지 않음.
print(df.corr()) # 피어슨 상관계수 : 공분산을 표준화 해서 일정한 기준이 준비됨. |0.3| 이상 일때 작업을 시도

# 일반적으로 
# 
# r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
# r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
# r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
# r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
# r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
# r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
# r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
"""

print('------------------------')
#파일 자료 읽기
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/drinking_water.csv")
print(data.head(3))
print(data.describe())
"""
          친밀도         적절성         만족도
count  264.000000  264.000000  264.000000
mean     2.928030    3.132576    3.094697
std      0.970345    0.859657    0.828744
min      1.000000    1.000000    1.000000
25%      2.000000    3.000000    3.000000
50%      3.000000    3.000000    3.000000
75%      4.000000    4.000000    4.000000
max      5.000000    5.000000    5.000000
"""
# plt.hist([np.std(data.친밀도), np.std(data.적절성), np.std(data.만족도)])
# plt.show()

print('\n공분산 출력----')
print(np.cov(data.친밀도, data.적절성)) # numpy
print(np.cov(data.친밀도, data.만족도))
print(data.cov()) # DataFrame

print('\n상관계수(r) 출력----')
print(np.corrcoef(data.친밀도, data.적절성)) # numpy
print(np.corrcoef(data.친밀도, data.만족도))
print(data.corr()) # 만족도와 적절성 : 뚜렷한 양적 선형관계 . method='pearson'이 기본값
print(data.corr(method='pearson')) # 정규성 O, 변수가 등간, 비율 척도 인 경우에 사용
print(data.corr(method='kendall'))
print(data.corr(method='spearman'))# 정규성 X, 서열 척도인 경우

print('')
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False)) # 만족도 기준 다른 변수와의 상관관계

# 시각화
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')
data.plot(kind = 'scatter', x='만족도', y='적절성')
plt.show()

# from pandas.plotting import scatter_matrix
# attr = ['친밀도','적절성','만족도']
# scatter_matrix(data[attr], figsize=(10, 6))
# plt.show()


# hitmap
import seaborn as sns
sns.heatmap(data.corr())
plt.show()

# hitmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()