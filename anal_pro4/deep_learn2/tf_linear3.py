#ex1) 단순선형회귀 - 경사하강법 함수 사용 1.x 
#실습 소스)

import tensorflow.compat.v1 as tf   # tensorflow 1.x 소스 실행 시
tf.disable_v2_behavior()            # tensorflow 1.x 소스 실행 시
import matplotlib.pyplot as plt

x_data = [1.,2.,3.,4.,5.]
y_data = [1.2,2.0,3.0,3.5,5.5]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

hypothesis = x * w + b
cost = tf.reduce_mean(tf.square(hypothesis - y))

print('\n경사하강법 메소드 사용------------')
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()   # Launch the graph in a session.
sess.run(tf.global_variables_initializer())

w_val = []
cost_val = []

for i in range(501):
    _, curr_cost, curr_w, curr_b = sess.run([train, cost, w, b], {x:x_data, y:y_data})
    w_val.append(curr_w)
    cost_val.append(curr_cost)
    if i  % 10 == 0:
        print(str(i) + ' cost:' + str(curr_cost) + ' weight:' + str(curr_w) +' b:' + str(curr_b))

plt.plot(w_val, cost_val)
plt.xlabel('w')
plt.ylabel('cost')
plt.show()


print('--회귀분석 모델로 Y 값 예측------------------')
print(sess.run(hypothesis, feed_dict={x:[5]}))        # [5.0563836]
print(sess.run(hypothesis, feed_dict={x:[2.5]}))      # [2.5046895]
print(sess.run(hypothesis, feed_dict={x:[1.5, 3.3]})) # [1.4840119 3.3212316]

print('\n 위 소스를 tf2.x 로 수행하기')
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers


x_data = [1.,2.,3.,4.,5.]
y_data = [1.2,2.0,3.0,3.5,5.5]

model = Sequential()
model.add(Dense(units=1, input_dim=1, activation = 'linear'))

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(x_data, y_data, epochs=100, batch_size=1, verbose=1)

loss_metrics = model.evaluate(x_data, y_data)
print('loss_metrics : ', loss_metrics)

import matplotlib.pyplot as plt
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'o')
plt.show()

print()
print('예측결과 : ', model.predict([1.345, 7.8]))

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data)))    #설명력 :  0.9495245052168231
#  설명력은 accuracy 와 다름.  회귀 직선과 데이터가 매우 밀접하게 분포.