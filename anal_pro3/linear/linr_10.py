# 다항식 처리 
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics._regression import mean_squared_error, r2_score

x = np.array([258,270,294,320,342,368,369,446,480,586])[:, np.newaxis]
print(x)
y = np.array([236,234,253,299,314,343,360,368,391,390])

lr = LinearRegression() #  일빈 회귀 모델용
pr = LinearRegression() # 일반 회귀 모델 - 다항식 추가

polyf = PolynomialFeatures(degree = 2)
x_quad = polyf.fit_transform(x)

#print(x_quad)
lr.fit(x, y)            # 일반 선형 회귀
x_fit = np.arange(250, 600, 10)[:, np.newaxis]
y_lin_fit = lr.predict(x_fit)
print(y_lin_fit)

print()
pr.fit(x_quad, y)            # 다항 회귀 모델
y_quad_fit = pr.predict(polyf.fit_transform(x_fit))
print(y_quad_fit)

# 시각화
import matplotlib.pyplot as plt
plt.scatter(x, y, label = 'train points')
plt.plot(x_fit, y_lin_fit, label = 'linear fit', linestyle='--')
plt.plot(x_fit, y_quad_fit, label = 'quadratic fit')
plt.legend()
plt.show()

print('-----------------------------------------')

y_lin_pred = lr.predict(x)
print('y_lin_pred : ', y_lin_pred)

print()
y_quad_pred = pr.predict(x_quad)
print('y_quad_pred : ',y_quad_pred)

#  성능 비교
print('MSE 비교  :  선형모델 : %.3f, 다항모델:%3f'%(mean_squared_error(y, y_lin_pred), mean_squared_error(y, y_quad_pred)))

print('결정 계수 비교  :  선형모델 : %.3f, 다항모델:%3f'%(r2_score(y, y_lin_pred), r2_score(y, y_quad_pred)))

# 데이터가  비선형인 경우에는 선형회귀 모델보다는 다항회귀 모델을 사용한 경우 성능이 우수함을 알 수 있다.

