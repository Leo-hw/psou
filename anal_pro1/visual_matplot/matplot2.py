# 주요 차트의 종류
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
plt.rc('font', family='malgun gothic')                        # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False           # 음수 부호 깨짐 방지

'''
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.hist(np.random.rand(10), bins = 10, alpha=0.9)
ax2.plot(np.random.rand(10))
plt.show()
'''

data = [50,80,100,70,90]
'''
plt.bar(range(len(data)), data)
plt.show()

error = np.random.randn(len(data))
plt.barh(range(len(data)), data, alpha=0.5, xerr = error)   # xerr 에러 바.(오차막대)
plt.show()
'''
'''
plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors=['yellow','red','blue','green'])
plt.title('원형 차트')
plt.show()

plt.boxplot(data)
plt.show()
'''
'''
# 버블 차트 : 산점도 차트에 점의 크기를 동적으로 표시
n = 30
np.random.seed(0)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (15 * np.random.rand(n)) **2
plt.scatter(x, y, c = color, s=scale)
plt.show()
'''
'''
# Series 자료로 차트
from pandas import Series
sdata = Series(np.random.randn(10).cumsum(), index= np.arange(0,100,10))
plt.plot(sdata)
plt.show()
'''
'''
# 시계열 자료 차트로 출력
import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4), index = pd.date_range('1/1/2000', periods=1000), columns=list('abcd'))
#print(fdata)
fdata = fdata.cumsum()
print(fdata.head())
plt.plot(fdata)
plt.show()
'''

print('\n ------------------------- matplotlib 의 기능 보강용 라이브러리 모듈 중 seaborn----------------------------------------')
import seaborn as sns
titanic = sns.load_dataset('titanic')             # seaborn 이 제공하는 dataset  의 일종
print(titanic.info())
#sns.distplot(titanic['age'])        # hist 는  distplot
#sns.boxplot(y='age', data = titanic, palette= 'Paired)
#sns.relplot(x='who', y = 'age', data= titanic)
#sns.countplot(x='class', data=titanic, hue='who')
titanic_pivot  = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
sns.heatmap(titanic_pivot, cmap=sns.light_palette('gray', as_cmap=True), annot=True, fmt='d')
print(titanic_pivot)
plt.show()


