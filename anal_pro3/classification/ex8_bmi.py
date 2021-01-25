# BMI 식을 이용하여, 원하는 양 만큼의 자료를 생성하여 파일로 저장 후 분류모델 적용
# BMI (체질량 지수) = 몸무게(kg) / (키(m))**2

#print(60/ (170/100)**2)
'''
import random

def calc_bmi(h,w):
    bmi = w / ( h / 100) ** 2
    if bmi < 18.5 : return 'thin'
    if bmi < 24 : return 'normal'
    return 'fat'

fp = open('bmi.csv', 'w', encoding='utf-8')
fp.write('height,weight,label\n')
# 무작위로 데이터 생성
cnt = {'thin':0, 'normal':0, 'fat':0}           # 건수를 위한 dict type 의 변수 선언

random.seed(12)

for i in range(50000):
    h = random.randint(150, 200)        # 키
    w = random.randint(35, 100)        # 몸무게
    label = calc_bmi(h,w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h, w, label))
    
fp.close()
print('ok')
'''
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tbl  = pd.read_csv('bmi.csv')
print(tbl.head(2))

# feature, label  로 분리하고 정규화
w = tbl['weight'] / 100
h = tbl['height'] / 200
wh = pd.concat([w,h], axis = 1)
print(wh.head(3), ' ', wh.shape)
label = tbl['label']
print(label.head(3), ' ', label.shape)

# 필수적으로 해야하는 과정은 아님.( 권장사항 ) - 범위 변수를 만들어서 범주형 수치화. 
# label = label.map({'thin':0, 'normal':1, 'fat':2})                  # 문자를 범주형 수치화
# print(label.head(3))
data_train, data_test, label_train, label_test = train_test_split(wh, label)
print(data_train.shape, data_test.shape)        # (37500, 2) (12500, 2)

# 분류 모델
model = svm.SVC().fit(data_train, label_train)          # train data 로 학습
pred = model.predict(data_test)         # test data 로 평가
print('예측값 : ',pred[:3],  '    실제값 : ', label_test[:3])
ac_score = metrics.accuracy_score(label_test, pred)
cl_report = metrics.classification_report(label_test, pred)
print('분류 정확도 : ', ac_score)
print('분류 보고서 : ', cl_report)

# 시각화
fig = plt.figure()
tbl  = pd.read_csv('bmi.csv', index_col = 2)
print(tbl.head())
def scatter_func(lbl, color):
    b = tbl.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label =lbl)
    
scatter_func('fat', 'red')
scatter_func('normal', 'yellow')
scatter_func('thin', 'blue')

plt.legend()
plt.savefig('bmitest.png')
plt.show()

    
    