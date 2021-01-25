# Keras 를 이용해 OR gate 논리 모델을 생성한 후 분류 결과 확인

import numpy as np
from tensorflow.keras.models import Sequential      # 선형 네트워크 스텍을 정의
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam, RMSprop


# 순서 1 : 데이터 수집 및 가공
x = np.array([[0,0], [0,1],[1,0],[1,1]])
y = np.array([0,1,1,1])
print(x)

# 순서 2 : 모델 생성
# model = Sequential([
#     Dense(input_dim = 2, units=1),
#     Activation('sigmoid')       # 이항 분류 -> sigmoid // 다항 분류 -> softmax
# ])
 
model = Sequential()
model.add(Dense(units = 1, input_dim = 2))
model.add(Activation('sigmoid'))

# 순서 3 : 모델 학습 과정 설정(컴파일)
# learning rate 를 주지 않는 경우
#model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])      # sgd = 확률적 경사하강법 Stochastic Gradient Descent
#model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])      # rmsprop = for minimizing cost
#model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])      # adam = en estos dias usa esto mas que otro

# learning rate 를 주는 경우
#model.compile(optimizer=SGD(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])      # momentum을 주어 해결
#model.compile(optimizer=SGD(lr=0.1, momentum=0.9), loss='binary_crossentropy', metrics=['accuracy'])      # momentum을 주어 해결(관성의 힘으로 지역적 최솟값을 벗어남)
#model.compile(optimizer=RMSprop(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])      # 여기는 모멘텀을 주지 않음 sgd의 보완방법
model.compile(optimizer=Adam(lr=0.01), loss='binary_crossentropy', metrics=['acc'])      # momentum을 주어 해결
#손실을 최소화 하는 방법으로... loss 손실함수 이항일 경우 binary crossentropy 


# 순서 4 : 모델 학습(train data)
model.fit(x,y, epochs=1000, batch_size=1, verbose=2)
# cost 를 최소화 하는데 이를 자동으로 진행 (back propagation 포함/ 여기서는 한번만 반복(epochs=1))

# 순서 5 : 모델 평가(test data)
loss_metrics = model.evaluate(x, y)         # loss_metrics[0] = loss//loss_metrics[1] = accuracy 
print('loss_metrics : ',loss_metrics)

"""
# 참고 : 모델 학습의 결과가 만족스러운 경우 모델을 저장 후 읽어서 예측을 한다.
model.save('test.hdf5')    # 모델 저장 시
from tensorflow.keras.models import load_model
model = load_model('test.hdf5')     # 저장된 모델 읽기
"""

# 순서 6 : 학습 결과 확인 - 예측값 출력.
pred = model.predict(x)
print(' 예측 결과 : ',pred.flatten()) 
print(' 예측 결과 : ',pred) 

pred = (model.predict(x) > 0.5).astype('int32')
print(' 예측 결과 : ',pred.flatten()) 
print(' 예측 결과 : ',pred) 
