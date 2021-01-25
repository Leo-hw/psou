from sklearn.neighbors import KNeighborsClassifier

# 이제 KNeighborsClassifier 모델을 생성해야 하는데, 이 때 n_neighbors로 k를 정해줘야 한다. 
# x 데이터를 분류를 할 때 k개의 이웃 중 거리가 가까운 이웃의 영향을 더 많이 받도록 가중치를 설정하려면 
# weights = "distance"를 지정해줄 수 있다.
kmodel = KNeighborsClassifier(n_neighbors = 3, weights = "distance")
train = [
  [5, 3, 1],
  [8, 7, 6],
  [4, 5, 7]
]
label = [0, 1, 1]

import matplotlib.pyplot as plt
plt.plot(train, 'o')
plt.xlim([-2, 5])
plt.ylim([0, 10])
plt.show()

# 그 다음 데이터를 .fit() 시켜준다. x 데이터는 여러 개의 차원으로 이루어진 배열(점들의 집합)이 될 거고, 
# y 데이터는 레이블(각 점들의 분류 결과)가 된다. 이 예제에서는 0 아니면 1로 분류되는 거다.
kmodel.fit(train, label)
pred = kmodel.predict(train)
print('pred : ', pred)

new_data = [
  [1, 2, 3],
  [6, 4, 2],
]
new_pred = kmodel.predict(new_data)
print('new_pred : ', new_pred)