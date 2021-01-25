# 베이지안 정리를 이용한 나이브 베이즈 분류 모델
# 조건부 확률을 이용 P (Label|features)

from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

#x = np.array([[1],[2],[3],[4],[5]])
x = np.array([1,2,3,4,5])
x = x[:, np.newaxis]            # 차원 확장  // 위와 동일한 결과.
print(x, x.shape)
y = np.array([1,3,5,7,9])

model = GaussianNB().fit(x, y)
print(model)
pred=  model.predict(x)
print(pred)
print('정확도 : ', metrics.accuracy_score(y, pred))

print()
# 새로운 값으로 분류
new_x = np.array([[0.5],[2],[9],[12],[0.1]])
new_pred = model.predict(new_x)

print(new_pred)

print('---------------------------------------------------------------------------------')
# One - hot encoding 된 자료로 연습 - np.eye()사용
x = '1,2,3,4,5'
x = x.split(',')
print('x : ', x)
x = np.eye(len(x))      # 단어 집합의 자료를 크기 만큼 벡터 차원으로 하고, 표현하고 싶은 자료에 인덱스를 1을 준다. 나머지는 0으로 채움  
print(x)
y = np.array([1,3,5,7,9])
model2 = GaussianNB().fit(x,y)
pred2= model2.predict(x)
print(pred2)

# One - hot encoding 된 자료로 연습 - OneHotEncoder사용
x = '1,2,3,4,5'
x = x.split(',')
print('x : ', x)
x = np.array(x)
x=x[:, np.newaxis]
one_hot = OneHotEncoder(categories='auto')
x = one_hot.fit_transform(x).toarray()
print(x)
y = np.array([1,3,5,7,9])
model3 = GaussianNB().fit(x,y)
pred3= model3.predict(x)
print(pred3)


print()
new_x = '0.7,2,3,-4,5.6'
new_x = new_x.split(',')
print('x : ', new_x)
new_x = np.array(new_x)
new_x=new_x[:, np.newaxis]
one_hot = OneHotEncoder(categories='auto')
new_x = one_hot.fit_transform(new_x).toarray()
print(new_x)


new_pred3= model3.predict(new_x)
print(new_pred3)

