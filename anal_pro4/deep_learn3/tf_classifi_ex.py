import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

np.random.seed(42)

# 데이터 준비하기
dataset = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/diabetes.csv', \
                     delimiter=',')

print(type(dataset)) # <class 'numpy.ndarray'>
print(dataset.shape) # (759, 9)
print(dataset[:1]) 

# train_test_split
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(dataset[:, 0:8],dataset[:, -1], test_size=0.3, random_state=123)  
print(x_train.shape)  # (531, 8)
print(x_test.shape)   # (228, 8)
print(y_train.shape)  # (531,)
print(y_test.shape)   # (228,)

# Sequential() ------------
model = Sequential()         
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=1000, batch_size=64)

scores = model.evaluate(x_test, y_test)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1] * 100)) 

pred = model.predict([[-0.29, 0.48, 0.18, -0.29,  0.11, 0.02, -0.53, -0.03]])
print('예측 결과 : ', pred)  #  [[0]]

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.show()

print()
# function api 사용 -------------
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

inputs = Input(shape=(8, ))
outputs1 = Dense(12, activation='relu')(inputs)
outputs2 = Dense(8, activation='relu')(outputs1)
outputs3 = Dense(1, activation='sigmoid')(outputs2)

model2 = Model(inputs, outputs3)

model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model2.fit(x_train, y_train, validation_split = 0.3, epochs=1000, batch_size=64)

scores = model2.evaluate(x_test, y_test)
print("%s: %.2f%%" %(model2.metrics_names[1], scores[1]*100))

pred = model2.predict([[-0.29, 0.48, 0.18, -0.29,  0.11, 0.02, -0.53, -0.03]])
print('예측 결과 : ', np.where(pred > 0.5, 1, 0))
