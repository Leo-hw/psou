# iris data 

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import pandas as pd
import seaborn as sns
plt.rc('font', family='malgun gothic')                        # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False           # 음수 부호 깨짐 방지

iris_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv')

print(iris_data.head(2))
print(iris_data.info())

plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.title('아이리스 데이터')
plt.show()

#pandas 의 시각화 기능
from pandas.plotting import scatter_matrix
iris_col = iris_data.loc[:, 'Sepal.Length':'Petal.Width']
scatter_matrix(iris_col)
plt.show()

# seaborn 기능
import seaborn as sns
sns.pairplot(iris_data, hue="Species")
plt.show()


