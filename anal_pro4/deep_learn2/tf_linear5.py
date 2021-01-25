# 다중 선형 회귀 모델 작성 후 TensorBoard 라는 시각화 툴을 사용
# TensorBoard - 모델의 구조 및 학습 진행 흐름을 시각화 해준다. 알고리즘의 동작을 확인할 수 있어 시행착오를 최소화 할 수 있다.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[70, 85,80],[71, 89,78],[50, 80,60],[69, 80,60],[50, 30,10]])
y = np.array([73,82,72,65,34])

print('Sequential Api 사용-------------------------------------')
model = Sequential()
#model.add(Dense(1, input_dim=1, activation = 'linear'))     # 레이어 1개
model.add(Dense(6, input_dim=3, activation = 'linear', name='a'))     # 레이어 3개
model.add(Dense(3, activation = 'linear', name = 'b'))
model.add(Dense(1, activation = 'linear', name ='c'))
print(model.summary())

opti = optimizers.Adam(lr=0.01)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model.fit(x, y, batch_size=1, epochs=100, verbose=0)
print(history.history)
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

print('predict : ', model.predict(x))
new_data  = np.array([[20,99,10], [90,90,90], [5,7,9]])
print('예상점수 : ',model.predict(new_data).flatten())

print('\nFunction Api 사용--------------------')
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape=(3,))
# outputs = Dense(1, activation = 'linear')(inputs)
# linear_model = Model(inputs, outputs)
outputs1 = Dense(6, activation = 'linear', name='a')(inputs)          # 레이어3개
outputs2 = Dense(3, activation = 'linear', name='b')(outputs1)
outputs = Dense(1, activation = 'linear', name='c')(outputs2)
linear_model = Model(inputs, outputs)


opti = optimizers.Adam(lr=0.01)
linear_model.compile(optimizer=opti, loss='mse', metrics=['mse'])



# 텐서보드 출력 준비
from tensorflow.keras.callbacks import TensorBoard
tb = TensorBoard(log_dir='.\\mylog', histogram_freq=1, write_graph=True) # histogram_freq을 표시하려면 1 안하려면 0
# -------------------------
"""
TensorBoard 실행 방법
py파일 실행 -> 아나콘다3 실행 
실행시킨 다음 패키지 주소복사해서 cd 바꿔주고 
tensorboard --logdir mylog/ 을 입력하면
(base) C:\work\pson\anal_pro4tf\deep_learn2>tensorboard --logdir mylog/
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.4.0 at http://localhost:6006/ (Press CTRL+C to quit)
위에 처럼 실행이됩니다. 
그중에 http://localhost:6006/ 이 주소를 웹브라우저에서 띄우시면 시각화 페이지 확인이 됩니다.
"""
# --------------------
# history = linear_model.fit(x, y, batch_size=1, epochs=100, verbose=1)# verbose=1이랑 0이랑 비교
history = linear_model.fit(x, y, batch_size=1, epochs=100, verbose=0,\
                           callbacks=[tb]) 
print(history.history)

print('predict :', linear_model.predict(x).flatten())
new_data = np.array([[20,99,19],[90,99,90],[5,7,9]])
print('예상점수 : ' , linear_model.predict(new_data).flatten())

'''
# 텐서보드 출력 준비
from tensorflow.keras.callbacks import TensorBoard
tb = TensorBoard(log_dir='.\\mylog', histogram_freq=1, write_graph=True)
# ------------------------------------------------------------------------

"""
TensorBoard 실행 방법
py파일 실행 -> 아나콘다3 실행 
실행시킨 다음 패키지 주소복사해서 cd 바꿔주고 
tensorboard --logdir mylog/ 을 입력하면
(base) C:\work\pson\anal_pro4tf\deep_learn2>tensorboard --logdir mylog/
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.4.0 at http://localhost:6006/ (Press CTRL+C to quit)
위에 처럼 실행이됩니다. 
그중에 http://localhost:6006/ 이 주소를 웹브라우저에서 띄우시면 시각화 페이지 확인이 됩니다.
"""

history = linear_model.fit(x, y, batch_size=1, epochs=100, verbose=0, \
                           callbacks=[tb])
print(history.history)
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

print('predict : ', linear_model.predict(x))
new_data  = np.array([[20,99,10], [90,90,90], [5,7,9]])
print('예상점수 : ',linear_model.predict(new_data).flatten())
'''