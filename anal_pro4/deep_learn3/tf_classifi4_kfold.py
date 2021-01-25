# k-fold cross validataion( k 겹 교차 검증) :  적은 양의 데이터로 과적합 방지가 가능한 모델 생성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import KFold, cross_val_score
import numpy as np

dataset = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/diabetes.csv', \
                     delimiter=',')

x = dataset[:, 0:-1]
y = dataset[:, -1]
print(x[:3])
print(y[:3])

model = Sequential([
    Dense(units=64, input_dim = 8, activation = 'relu'),
    Dense(units=32, activation = 'relu'),
    Dense(units=1,  activation = 'sigmoid'),
                    
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(x, y, epochs=100, batch_size = 32, verbose=1)
print(model.evaluate(x,y))
print('----------------------------------------')

print('\n k겹 교차검증-------------------------------')
def build_model():
    model = Sequential()
    model.add(Dense(64, input_dim = 8, activation = 'relu'))
    model.add(Dense(32, activation = 'relu'))
    model.add(Dense(1, activation = 'sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
    return model

# 함수를 호출하여 모델 네트워크 얻기
estimatorModel = KerasClassifier(build_fn = build_model, epochs= 100, batch_size=32, verbose=1)

kfold = KFold(n_splits= 5, shuffle = True, random_state = 12)
print(cross_val_score(estimatorModel,x, y, cv =kfold))
estimatorModel.fit(x, y, epochs=100, batch_size = 32, verbose=1)
#print(estimatorModel.evaluate(x,y))     # AttributeError: 'KerasClassifier' object has no attribute 'evaluate'
# 케라스에는 evaluate가 없음.

from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(y, estimatorModel.predict(x)))

pred = estimatorModel.predict(x[:3, :])
print('pred : ' , pred)