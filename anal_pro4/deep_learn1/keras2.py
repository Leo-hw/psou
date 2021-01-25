# Keras 를 이용해 OR gate 논리 모델을 생성한 후 분류 결과 확인

import numpy as np
from tensorflow.keras.models import Sequential      # 선형 네트워크 스텍을 정의
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam, RMSprop


# 순서 1 : 데이터 수집 및 가공
x = np.array([[0,0], [0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])     #and 


"""
model = Sequential()
model.add(Dense(5, input_dim=2))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))        # 이항 분류이므로 출력을 활성화 함수는 sigmoid
"""
model = Sequential()
model.add(Dense(5, input_dim=2, activation = 'relu'))
model.add(Dense(5, input_dim=2, activation = 'relu'))           # hidden layer
model.add(Dense(1, activation = 'sigmoid'))     # 출력할 때 이항이므로 sigmoid // 다항이면 softmax


print()
print(model.summary())          # 전체 구조에 대한 parameter
print('---------------------------------------')
print('input(입력 구조) : ',model.input)          # 입력 구조
print('output(출력 구조) : ',model.output)         # 출력 구조
print('weights(가중치와 편향) : ',model.weights)            # 가중치와 편향
print('---------------------------------------')

model.compile(optimizer=Adam(0.01), loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x, y, epochs=1000, batch_size=1, verbose=1)
loss_metrics = model.evaluate(x, y)
print('loss_metrics : ', loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
print('pred : ', pred.flatten())

print(' ****'*10)
print('loss : ', history.history['loss'])
print('acc : ', history.history['accuracy'])



import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label = 'train loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(loc = 'best')                #  4 사분면 중 위치를 잡아주는 것
plt.show()


import pandas as pd
pd.DataFrame(history.history).plot(figsize=(8,5))
plt.show()
