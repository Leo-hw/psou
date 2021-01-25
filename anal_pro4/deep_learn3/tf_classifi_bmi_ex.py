import  numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.metrics._classification import accuracy_score,\
    classification_report
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bmi.csv')
print(df.head())
print(' --------')
model = Sequential()
model.add(Dense(10, input_dim=4, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics = ['acc'])
print(model.summary())


'''
#표준화
scaler = StandardScaler()
x_scale = scaler.fit_transform(x)

x_train_x_test, y_train, y_test = train_test_split(x, y, )

model.fit(x_train, y_train, epochs=50, batch_size=10)
print('모델검증 : ', model.evaluate(x_test, y_test))

print()
y_pred = np.argmax(model.predict(x_test), axis = 1)
print('예측값: ', y_pred)
real_y = np.argmax(y_test, axis =1).reshape(-1,1)
print('실제값: ', real_y.ravel())
pr
int('분류 실패 수 :',(y_pred.ravel() != real_y).sum( ))
print()

from sklearn.metrics import confusion_matrix, classification_report
print('confusion_matrix : \n', confusion_matrix(real_y, y_pred))
print('accuracy : ', accuracy_score(real_y, y_pred))
print('classification_report :\n ', classification_report(real_y, y_pred))

print('\n새로운 값으로 분류 예측 ----------------------------------')
new_x = [[5.1,3.5,1.4,0.2], [4.6,3.0, 1.4,2.2],[1.6,3.8,5.4,8.2]]
new_x = StandardScaler().fit_transform(new_x)
new_pred = model.predict(new_x)
print('new_pred : ', new_pred)
print('new_pred : ', np.argmax(new_pred, axis=1).flatten())
'''
