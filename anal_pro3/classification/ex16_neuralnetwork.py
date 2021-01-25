# Perceptron : 단층 신경망(뉴런, 노드)으로 input_data * 가중치의 합에 대해 임계값(활성화 함수)을 기준으로 이항분류가 가능 
# 단층 신경망으로 논리회로 분류 - 단층 신경망으로 xor은 분류 불가능
import numpy as np
from sklearn.linear_model import Perceptron

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
#label = np.array([0,0,0,1])    #and
#label = np.array([0,1,1,1])     # or
label = np.array([0,1,1,0])     #xor 배타적인 or

ml = Perceptron(max_iter = 1000).fit(feature, label)
print(ml)
print(ml.predict(feature))


print('\n 다층 신경망으로 xor 문제 해결')
from sklearn.neural_network import MLPClassifier
#ml2 = MLPClassifier(hidden_layer_sizes=50).fit(feature, label)
#ml2 = MLPClassifier(hidden_layer_sizes=(10,10,10)).fit(feature, label)
ml2 = MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter=100, verbose=1, learning_rate_init=0.01).fit(feature, label)     # loss = 잔차
# 조기 중단 ( 학습을 하다가 잔차가 더이상 줄어들지 않는 시점에 자동으로 중단)
# max_iter : 학습횟수
# learning_rate_init : 학습율 ( 요게 알파...? Gradient descent 
print(ml2)
print(ml2.predict(feature))
