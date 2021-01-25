# 데이터 간 단위의 차이가 클 경우 정규화 / 표준화 권장
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler, RobustScaler
# MinMaxScaler : 정규화 ( 요소값 - 최소값) / (최대값 - 최소값)
# StandardScaler : 표준화 ( 요소값 - 평균) / 표준편차
# RobustScaler : 중앙값과 IQR을 사용, 이상치의 영향을 최소화 시키고자 할 때 유용.

import pandas as pd
import numpy as np

np.random.seed(123)

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv')
print(data.head())
del data['no']
print(data.head())

# scaling : 정규화1
scaler = MinMaxScaler(feature_range=(0,1))
#scaler = MinMaxScaler()    # 기본값이 feature_range=(0,1)
xy = scaler.fit_transform(data)
print(xy[:2])
abc = scaler.inverse_transform(xy)          # 원래대로 돌리기. invers_transform
print(abc[:2])

# scaling : 정규화 2
xy = minmax_scale(data, axis=0, copy = True)         # 원본데이터 보존을 원하는 경우(원본을 보존한 후 복사해서 정규화)
print(xy[:2])

#  train / test 로 분리 : 과적합 방지 - 편향된 분리 X, 시계열데이터인 경우에는 shuffling 하면 안됨, 중복 데이터는 없도록 한다.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(xy[:, 0:-1], xy[:, -1], test_size=0.3, random_state=123)
print(x_train[:2],'  ' ,x_train.shape)      # tv radio newpaper (140, 3)
print(x_test[:2],'  ' ,x_test.shape)    # (60,3)
print(y_train[:2],'  ' ,y_train.shape)  # sales (140, )

model = Sequential()
# model.add(Dense(1, input_dim = 3))
# model.add(Activation('linear'))

model.add(Dense(1, input_dim = 3))
model.add(Activation('linear'))     # 위에 거에 넣을 수도 있음
model.add(Dense(20))
model.add(Activation('linear'))
model.add(Dense(10))
model.add(Activation('linear'))
model.add(Dense(1))
model.add(Activation('linear'))


print(model.summary())
import tensorflow as tf
tf.keras.utils.plot_model(model, 'abc.png')     # 모델의 순차적 계층을 이미지로 저장 가능.

model.compile(optimizer=Adam(lr=0.001), loss='mse', metrics=['mse'])
model.fit(x_train, y_train, epochs=100, batch_size=64, verbose=1,\
          validation_split=0.3)     # 과적합 방지 : validation_split = 0.3         train data 를 30%를 학습 시 검정 데이터로 사용

loss = model.evaluate(x_test, y_test)   # 모델 평가는 test dataset 을 사용
print('loss : ', loss)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_test, model.predict(x_test)))

pred = model.predict(x_test) 
print('실제값 : ', y_test[:3], ', 예측값 : ', pred[:3])

