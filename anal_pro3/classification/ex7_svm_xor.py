# SVM 으로 XOR 분류 모델 작성
xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

xor_df = pd.DataFrame(xor_data)
print(xor_df)
feature = np.array(xor_df.iloc[:, 0:2])
label = np.array(xor_df.iloc[:, 2])
print(feature)
print(label)

'''
#print('LogisticRegression 으로 분류')
#model = LogisticRegression()
'''
# SVM 알고리즘(SVC) 으로 분류
#model = svm.SVC()
model = svm.SVC(C=100)        # C 값이 커지면 overfitting 발생확률이 높아짐
#model = svm.LinearSVC(C=5)

model.fit(feature, label)
pred = model.predict(feature)
print('예측값: ', pred)

print()
acc = metrics.accuracy_score(label, pred)
print('accuracy : ', acc)

ac_report = metrics.classification_report(label, pred)
print(ac_report)

