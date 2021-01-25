# 와인 분류 ( Red, White)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import pandas as pd
import  numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf

wdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/wine.csv')
print(wdf.head())
print(wdf.info())
print(wdf.iloc[:, 12].unique())

dataset = wdf.values
x = dataset[:, 0:12]        # feature
y = dataset[:, -1]          # label(class)
print(x)
print(y)

# 과적합 방지 목적// data 양이 적을 때는  k-fold

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 123)   # 수업 목적이라 random_state 를 정해줌.
print(x_train.shape, x_test.shape, y_train.shape)   #(4547, 12) (1949, 12) (4547,)

# 추가적으로 outlier(이상치), 결측치 도 봐야함


# 모델 설정
model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))       
model.add(tf.keras.layers.BatchNormalization())     # 배치 정규화 - Gradient loss 등의 문제 해결
model.add(Dense(15, activation='relu'))                 # hidden layer 는 relu
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))       # 이항분류 이므로 출력시에는 sigmoid
# 레이어의 갯수가 많을 수록 좋은 것은 아님 => 계속 돌려봐야함(for 문) // 정확도가 높은 것 사용

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])       # 여기서 accuracy 라고 써서 밑에도 accuracy임(여기에 acc라고 적으면 acc)

# fit() 이전의 훈련 되지 않은 모델에 대해서 evaluate
loss, acc = model.evaluate(x_train, y_train, batch_size=32, verbose=2)
print('훈련되지 않은 모델 평가 : {:5.2f}%, \t loss : {}'.format(acc * 100, loss))     # 훈련되지 않은 모델 평가 : 74.88%,      loss : 0.49585625529289246


# 모델 실행 및 저장
# 학습 시 모델 저장 폴더 설정
MODEL_DIR = './winemodel/'
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# 학습시 모니터링의 결과를 파일로 저장 가능
chkpoint = ModelCheckpoint(filepath='./winemodel/wine.hdf5', monitor='loss', verbose=2, save_best_only=True)    # 최적의 값으로 계속 덮어씌움

# 진행되는 내용 모두 저장
# modelpath = "./winemodel/{epoch:02d}-{loss:4f}.hdf5"            # epoch 만큼 계속 들어감
# chkpoint = ModelCheckpoint(filepath=modelpath, monitor='loss', verbose=2, save_best_only=True)
# loss 값이 가장 적을 때의 값을 저장 => 최적의 모델을 확인 할 수 있다.


# 학습 조기 종료 : loss 가 떨어지거나 accuracy가 더 이상 오르지 않는 ( 변화가 없는 )경우 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5)
history = model.fit(x_train, y_train,validation_split=0.3 , batch_size=64, epochs = 1000, verbose=2, callbacks = [early_stop, chkpoint])      # 조기 종료와 동시에 저장
# validation_data = 잘라놓은 데이터를 쓰고 싶을 때,
# validation _split = 데이터를 잘라서 쓰고 싶을 때 - 번갈아가면서 잘라서 씀.

# 파일로 저장된 결과값 읽기
#model.load_weights(filepath='./winemodel/wine.hdf5')

loss, acc = model.evaluate(x_test, y_test, batch_size=64, verbose=2)
print('훈련된 모델 평가 : {:5.2f}%, \t loss : {}'.format(acc * 100, loss))  #훈련된 모델 평가 : 97.69%,      loss : 0.087151899933815

print()
print('history: ', history.history)

vloss = history.history['val_loss']
print('vloss :', vloss, len(vloss))
loss = history.history['loss']
print('loss :', loss, len(loss))

acc = history.history['accuracy']
print('acc :', acc)

# 시각화 
epoch_len = np.arange(len(acc))
plt.plot(epoch_len, loss)
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

epoch_len = np.arange(len(acc))
plt.plot(epoch_len, acc)
plt.xlabel('epochs')
plt.ylabel('acc')
plt.show()

print()
# 예측
np.set_printoptions(suppress=True)
new_data = x_test[:5, :]
print(new_data)
pred = model.predict(new_data)
print('pred : ', np.where(pred>0.5, 1, 0).flatten())