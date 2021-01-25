# agg() : 함수를 수행하는 함수, apply()


import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tips.csv')
print(tips.info())
print(tips.head(3))
tips['gender'] = tips['sex']
del tips['sex']
print(tips.head(3))

# 그룹별 작업 : 성별, 흡연자별 그룹화
tip_pct_group = tips['tip'].groupby([tips['gender'],tips['smoker']])
print(tip_pct_group)
print(tip_pct_group.sum())
print(tip_pct_group.mean())
print(tip_pct_group.min())

result = tip_pct_group.describe()
print(result)

# agg()
print(tip_pct_group.agg('sum'))
print(tip_pct_group.agg('max'))
print(tip_pct_group.agg('min'))
print(tip_pct_group.agg('var'))

print('-----------------------------------')
# 사용자 정의 함수
def diffFunc(group):
    diff = group.max() - group.min()
    return diff

result2 = tip_pct_group.agg(['sum', 'mean', 'max', 'var', diffFunc])
print(result2, type(result2))

result2.plot(kind='barh', title='agg result', stacked=True)
plt.show()

print()
# apply()
print(tip_pct_group.agg('sum'))         # agg 는 따옴표(')를 두르고,
print(tip_pct_group.apply(sum))         # apply 는 따옴표(')를 두르지 않음

