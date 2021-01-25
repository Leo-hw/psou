# 비선형 데이터의 경우 : 선형 회귀 모델을 다항 회귀로 변환

# 입력 데이터 특징 변환으로 선형 모델 개선

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

plt.scatter(x,y)
plt.show()

# 선형 모델 작성 - 위 비선형 자료를 이용
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis]
#print(x)
model = LinearRegression().fit(x,y)
ypred = model.predict(x)
print(ypred)
'''
plt.scatter(x,y)
plt.plot(x, ypred, c = 'red')
plt.show()
'''
print('---------------------------------')
# 모델에 유연성을 부여하기 위해 특징(feature) 을 추가.
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 2, include_bias = False) # degree 열의 갯수
x2 = poly.fit_transform(x)
print(x2)

model2 = LinearRegression().fit(x2,y)
ypred2 = model2.predict(x2)
print(ypred2)

plt.scatter(x,y)
plt.plot(x, ypred2, c = 'red')
plt.show()
