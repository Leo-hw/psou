# Liner Regression 모델 생성 시 오버 피팅 (train data에 최적화된 모델이 새로운 데이터에 예측을 떨어뜨리는 현상)이 발생 가능
# 오버피팅 방지를 Ridge, Lasso, ElasticNet 등의 클래스를 이용

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
 
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
iris_df["target_names"] = iris.target_names[iris.target]
print(iris_df[:5])
 
# 훈련세트, 테스트세트 나누기
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(iris_df, test_size = 0.3)
 
print(train_set.shape)
print(test_set.shape)
 
print('\nLinearRegression)')
# 회귀분석 방법 1 - 선형 회귀(최소제곱)
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt
 
model = lm().fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])
print(model.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])) 
print(model.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))   
print(model.coef_)      #[[ 0.40847816]]
print(model.intercept_) #[-0.33677518]
print('predict : ', model.predict(test_set.iloc[:, [2]]))
 
#plot
plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='black')
plt.plot(test_set.iloc[:, [2]], model.predict(test_set.iloc[:, [2]]))
plt.show()
 
print('\nRidge')
# 회귀분석 방법 2 - Ridge: alpha값을 조정(가중치 제곱합을 최소화)하여 과대/과소적합을 피한다. 다중공선성 문제 처리에 효과적.
from sklearn.linear_model import Ridge
model_ridge = Ridge(alpha=10).fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])
 
#점수
print(model_ridge.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])) #0.91923658601
print(model_ridge.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))   #0.935219182367
print('ridge predict : ', model_ridge.predict(test_set.iloc[:, [2]]))
#plot
plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='red')
plt.plot(test_set.iloc[:, [2]], model_ridge.predict(test_set.iloc[:, [2]]))
plt.show()
 
print('\nLasso')
# 회귀분석 방법 3 - Lasso: alpha값을 조정(가중치 절대값의 합을 최소화)하여 과대/과소적합을 피한다.
from sklearn.linear_model import Lasso

model_lasso = Lasso(alpha=0.1, max_iter=1000).fit(X=train_set.iloc[:, [0,1,2]], y=train_set.iloc[:, [3]])

#점수
"""
print(model_lasso.score(X=train_set.iloc[:, [0,1,2]], y=train_set.iloc[:, [3]])) #0.921241848687
print(model_lasso.score(X=test_set.iloc[:, [0,1,2]], y=test_set.iloc[:, [3]]))   #0.913186971647
print('사용한 특성수 : ', np.sum(model_lasso.coef_ != 0))   # 사용한 특성수 :  1
print('lasso predict : ', model_lasso.predict(test_set.iloc[:, [2]]))
plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='blue')
plt.plot(test_set.iloc[:, [2]], model_lasso.predict(test_set.iloc[:, [2]]))

plt.show()
"""
# 회귀분석 방법 4 - Elastic Net 회귀모형 : Ridge + Lasso