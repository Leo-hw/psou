import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bmi.csv')

print(data.head(3))
print(data.info())
replace = {'thin':0,'normal':1,'fat':2}
data = data.replace({'label':replace})
x = np.array(data.iloc[:,:-1])
# print(x.shape)
y_data = np.array(data.iloc[:,-1])
# print(x_data)
# print(y_data)
onehot = OneHotEncoder(categories='auto')
y = onehot.fit_transform(y_data[:,np.newaxis]).toarray()
# print(x)
# print(y)

# 표준화
'''
scaler = StandardScaler()
x = scaler.fit_transform(x)
print(x[:2])
'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
print(x_train.shape,' ', x_test.shape) # (14000, 2)   (6000, 2)
print(y_train.shape,' ', y_test.shape) # (14000, 3)   (6000, 3)

model = Sequential()
model.add(Dense(32, input_dim=2, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8,  activation='relu'))
model.add(Dense(3, activation='softmax'))
# print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x_train,y_train, epochs=20, batch_size=32,verbose=2)
print('모델 검증 : ', model.evaluate(x_test, y_test))
print('----------------')
y_pred = np.argmax(model.predict(x_test), axis= 1)
print('예측값 :', y_pred)
real_y = np.argmax(y_test, axis =1).reshape(-1,1)
print('실제값 :', real_y.ravel())
print('-------------')


plt.figure(figsize=(12,4))
plt.subplot(121)
plt.plot(history.history['loss'],'b-',label='loss')
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'],'r-',label='acc')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
plt.legend()
plt.show()


plt.figure()
plt.plot([0, 1], [0, 1], 'k--')
pred_y = model.predict(x_test)
fpr, tpr, _ = roc_curve(y_test.ravel(),pred_y.ravel())
print('AUC: ',auc(fpr,tpr))
plt.plot(fpr, tpr)    
plt.xlabel('False Positive rate')
plt.ylabel('True Positive rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

print('confusion_matrix \n',confusion_matrix(real_y, y_pred))
print('accuracy : ', accuracy_score(real_y, y_pred))
print('classification_report : \n', classification_report(real_y, y_pred))

height = float(input('height : '))
weight = float(input('weight : '))
new_x = [[height,weight]]
new_pred = model.predict(new_x)
print('new_pred : ', np.argmax(new_pred, axis = 1))
