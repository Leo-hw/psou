# 3 ways to create a Keras model with TensorFlow 2.x
# (Sequential, Functional, and Model Subclassing)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np

x_data = np.array([1,2,3,4,5], dtype = np.float32)      # 공부시간
y_data = np.array([11,32,53,58,65], dtype =np.float32)      # 성적
print(np.corrcoef(x_data, y_data))      # 상관 관계 0.959 공부 시간이 늘어날 수록 성적이 좋아짐(인과 관계가 있음)

print('\nSequential api 사용------------')

############################## 선형 회귀 분석 방법 1 : Sequential api 사용
model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))
#model.add(Dense(1,  activation='linear'))        # layer 추가

opti = optimizers.SGD(lr = 0.001)
model.compile(optimizer=opti, loss='mse', metrics=['mse', 'mae'])       # mae 가 mse 보다 이상치에 덜 민감

model.fit(x=x_data, y = y_data, batch_size=1, epochs=100, verbose=0)
loss_metrics = model.evaluate(x_data, y_data)


from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data)))    #설명력 :  0.9204

print('실제값 : ', y_data)
print('예측값 : ', model.predict(x_data).flatten())
print('새로운 공부 시간에 대한 예상 점수', model.predict([2.3, 6.8, 7.0]).flatten())

"""
# 시각화
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
plt.xlabel('공부시간')
plt.ylabel('시험 성적')
plt.show()
"""
############################## 선형 회귀 분석 방법 2 : Functional api 사용 - 방법1 보다 다소 복잡해보이나 유연한 모델 작성이 가능. 여러 층의 자원을 공유 가능
print('\n Functional api 사용 ==========================')
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape=(1,))      # input layer 를 생성
#outputs = Dense(1, activation='linear')(inputs)
outputs1 = Dense(5, activation='linear')(inputs)        # 복수의 레이어 인 경우
outputs2 = Dense(1, activation='linear')(outputs1)
model2  = Model(inputs, outputs2)


opti = optimizers.SGD(lr = 0.001)
model2.compile(optimizer=opti, loss='mse', metrics=['mse', 'mae'])       # mae 가 mse 보다 이상치에 덜 민감

model2.fit(x=x_data, y = y_data, batch_size=1, epochs=100, verbose=0)
loss_metrics = model2.evaluate(x_data, y_data)
print('loss_metrics  : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model2.predict(x_data)))    #설명력 :  0.9204

print('실제값 : ', y_data)
print('예측값 : ', model2.predict(x_data).flatten())
print('새로운 공부 시간에 대한 예상 점수', model2.predict([2.3, 6.8, 7.0]).flatten())

############################## 선형 회귀 분석 방법 3 : Subclassing api 사용 // 방법1, 2 - 선언적인 방법//   방법3- 동적인 구조가 필요할 때 사용
print('\n subclassing api 사용------------------------------')
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(2, activation = 'linear')
        self.d2 = Dense(1, activation = 'linear')
        
    def call(self, x):          # 모델.fit() 모델.evaluate(), 모델.predict()
        # 파이썬 작업이 가능. 계산, for, if, tensor 처리...
        x = self.d1(x)
        return self.d2(x)
    
model3 = MyModel()

opti = optimizers.SGD(lr = 0.001)
model3.compile(optimizer=opti, loss='mse', metrics=['mse', 'mae'])       # mae 가 mse 보다 이상치에 덜 민감

model3.fit(x=x_data, y = y_data, batch_size=1, epochs=90, verbose=0)
loss_metrics = model3.evaluate(x_data, y_data)
print('loss_metrics  : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model3.predict(x_data)))    #설명력 :  0.9204

print('실제값 : ', y_data)
print('예측값 : ', model3.predict(x_data).flatten())
print('새로운 공부 시간에 대한 예상 점수', model3.predict([2.3, 6.8, 7.0]).flatten())

print('\n subclassing api 사용 2  ------------------------------')
from tensorflow.keras.layers import Layer

class Linear(Layer):
    def __init__(self, units=1):
        super(Linear, self).__init__()
        self.units = units
        
    def build(self, input_shape):       # call을 호출
        self.w = self.add_weight(shape=(input_shape[-1], self.units), \
                                 initializer = 'random_normal', trainable = True)               # trainable : 역전파 back propagation
        self.b = self.add_weight(shape=(self.units), \
                                 initializer = 'zeros', trainable = True)               # bias : 출력계수와 맞춰야함                
        
    def call(self, inputs):
        return tf.matmul(inputs, self.w) +self.b

class MyMlp(Model):
    def __init__(self):
        super(MyMlp, self).__init__()
        self.linear_1  = Linear(1)          # 레이어가 1개 인 경우
        #self.linear_1  = Linear(2)        # 레이어가 2개 인 경우
        #self.linear_2  = Linear(1)
        
    def call(self, inputs): # Linear 의 build 호출
        return self.linear_1(inputs)
    
model4 = MyMlp()

opti = optimizers.SGD(lr = 0.001)
model4.compile(optimizer=opti, loss='mse', metrics=['mse', 'mae'])       # mae 가 mse 보다 이상치에 덜 민감

model4.fit(x=x_data, y = y_data, batch_size=1, epochs=90, verbose=0)
loss_metrics = model4.evaluate(x_data, y_data)
print('loss_metrics  : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model4.predict(x_data)))    #설명력 :  0.9204

print('실제값 : ', y_data)
print('예측값 : ', model4.predict(x_data).flatten())
print('새로운 공부 시간에 대한 예상 점수', model4.predict([2.3, 6.8, 7.0]).flatten())
