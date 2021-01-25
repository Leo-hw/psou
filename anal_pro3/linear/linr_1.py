# 선형회귀 분석 : 추세선의 기울기와 절편 값 구하기 - 최소 제곱법 이용.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,])
y = np.array([-1,0.2, 0.9, 2.1])
print(np.corrcoef(x,y)[0,1])

# plt.plot(x,y, 's')
# plt.grid(True)
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)

# 최소 자승법으로 기울기, 절편
m,c  = np.linalg.lstsq(A, y, rcond=None)[0]
print('기울기:', m,' , 절편 :', c)
# y = mx+ c 식을 얻음
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x+c, 'r', label = 'Fitted line')
plt.legend()
plt.show()
print(0.9999999999999997 *1 + -0.9499999999999992)
print(0.9999999999999997 *2 + -0.9499999999999992)
print(0.9999999999999997 *100 + -0.9499999999999992)