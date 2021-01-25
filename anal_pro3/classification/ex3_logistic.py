# softmax 활성화 함수

import numpy as np
import matplotlib.pyplot as plt
'''
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
 
x = np.array([3.4,2.0,1.8])
 
y = softmax(x)
print(y)
print(np.sum(y))
ratio = y
labels = y

plt.pie(ratio, labels=labels, shadow=True, startangle=90)
plt.show()
'''
from sklearn import datasets
from sklearn.linear_model import LogisticRegression     # softmax 함수를 사용해서 다항 분류
import numpy as np


iris = datasets.load_iris()
#print(iris.DESCR)
print(iris.keys())
print(iris.target)
x = iris['data'][:,[ 3]]  # 꽃잎 너비 칼럼만 사용
print(x[:10])       # [0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1]
y = (iris['target']== 2).astype(np.int)     # setosa + versicolor , verginica  <= 두 그룹으로 나눔
print(y)

log_reg = LogisticRegression()
print(log_reg)
log_reg.fit(x,y)

x_new = np.linspace(0, 3, 1000).reshape(-1,1)
print(x_new.shape)
y_proba = log_reg.predict_proba(x_new)
#print(y_proba)      # [[9.99250016e-01 7.49984089e-04]...

import matplotlib.pyplot as plt
plt.plot(x_new, y_proba[:, 1], 'r-', label = 'virginica')
plt.plot(x_new, y_proba[:, 0],'b--',  label = 'not virginica')
plt.xlabel('petal_width')
plt.legend()
plt.show()


print()
print(log_reg.predict([[1.5],[1.7]]))         #[0 1]
print(log_reg.predict([[2.5],[0.7]]))        #[1 0]
print(log_reg.predict_proba([[2.5],[0.7]]))