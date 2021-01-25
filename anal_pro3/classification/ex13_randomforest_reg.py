
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston

boston = load_boston()
print(boston.DESCR)

dfx = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=['MEDV'])
df = pd.concat([dfx, dfy], axis= 1)
print(df.head(3))

'''
#시각화
cols = ['MEDV', 'RM', 'AGE', 'LSTAT']
sns.pairplot(df[cols])
plt.show()
'''

x = df[['LSTAT']].values        # 독립 변수
y = df['MEDV'].values       # 종속 변수

print(x[0])
print(y[0])

# 실습 1 : DecisionTreeRegressor
#model = DecisionTreeRegressor(max_depth = 3).fit(x, y)

# 실습 2 : DecisionTreeRegressor
model = RandomForestRegressor(n_estimators=100, \
                              criterion = 'mse', random_state=123, n_jobs=1).fit(x, y)         # mse 를 쓰는 이유...? 여기서는 entropy 나 이런거 쓰지 않음

print('predict : ' ,model.predict(x)[:5])
r2 = r2_score(y, model.predict(x))
print('결정계수(설명력) : ', r2)

print('\n train / test 로 분리해서 작업 ---- ')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 123)
model.fit(x_train, y_train)
print('model2 : ', model.predict(x_test)[:5])

# 결정계수
trainR2 = r2_score(y_train, model.predict(x_train))
print('학습데이터로 작업한 결정 계수 : ',trainR2)

testR2 = r2_score(y_test, model.predict(x_test))
print('검정데이터로 작업한 결정 계수 : ',testR2)

# 학습데이터로 작업한 결정 계수 :  0.908199247049924
# 검정데이터로 작업한 결정 계수 :  0.5805382105034671
### 독립 변수의 갯수를 늘리면 둘 사이의 차이가 줄어들 수 있다.

# 새값으로 집 값 예측
import numpy as np
#print(x_test[:3])
x_new = np.array([[10],[50],[1]])        # LSTAT
print('예상 집값 : ', model.predict(x_new))     # MEDV
