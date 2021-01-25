# 모델의 정확도가 높을수록 비용함수 값은 낮아지며, 모델의 정확도가 낮으면 비용함수가 높아진다.

import math
import numpy as np
real = np.array([10, 9, 3, 2, 11])        # 실제 값
#pred = np.array([11, 5, 2, 4, 3])         # 모델의 예측 값(가정)
pred = np.array([10, 8, 4, 3, 11])         # 모델의 예측 값(가정)
# 모델의 예측 값과 실제 값의 차이가 적을수록 cost (비용함수)의 값이 작아지고 정확도가 높아짐.

print(np.corrcoef(pred, real))      # 0.4563833        #0.98939824

print()
cost = 0
for i in range(5):
    cost += math.pow(pred[i] - real[i], 2)
    print(cost)
    
print()
print(cost / len(pred))
    
print('---------------------------------------------------------------------')
# 비용함수(Cost)와 가중치(Weights)의 변화값을 시각화
import tensorflow as tf
import matplotlib.pyplot as plt

x = [1,2,3,4,5] # feature
#y = [1,2,3,4,5] # label
y = [2,4,6,8,10] # label
b = 0

w_val = []
cost_val = []

for i in range(-30, 50):
    feed_w = i * 0.1                # 0.1 은 learning rate (학습률)
    #print(feed_w)
    hypothesis = tf.multiply(feed_w, x) + b
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    cost_val.append(cost)
    w_val.append(feed_w)
    print((str(i) + ' :  cost :  '+ str(cost.numpy())+ ',  weght : ' + str(feed_w)))        # 10 :  cost :  0.0,  weght : 1.0
    
plt.plot(w_val, cost_val, 'o')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()
