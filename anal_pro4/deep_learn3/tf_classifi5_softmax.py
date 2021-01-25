# 다항 분류 : 출력층의 화성화 함수를 softmax 로 사용

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# dastaset
xdata = np.random.random((1000, 12))
ydata = np.random.randint(10, size = (1000, 1))
print(xdata, xdata.shape)
#print(ydata, ydata.shape) 
ydata = to_categorical(ydata, num_classes=10)
print(ydata)
print(xdata[:1])
print(ydata[:1])


# model
model = Sequential()
model.add(Dense(100, input_shape=(12,), activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])

history = model.fit(xdata, ydata, epochs=500, batch_size=32, verbose=2)
model_eval = model.evaluate(xdata, ydata)
print('model_eval : ', model_eval)
print('pred : ', np.argmax(model.predict(xdata[[0]])))
print('pred : ', np.argmax(model.predict(xdata[:1])))
print('pred : ', model.predict(xdata[:1]))

print('실제값: ', ydata[:5])
print('실제값: ', [np.argmax(i) for i in ydata[:5]])
print('예측값: ', xdata[:5])
print('예측값: ', [np.argmax(i) for i in model.predict(xdata[:5])])

# 시각화
plt.plot(history.history['loss'], label = 'loss')
plt.plot(history.history['acc'], label = 'acc')
plt.xlabel('epochs')
plt.legend()
plt.show()

print()
# 새 데이터 예측
x_new = np.random.random([1, 12])
pred = model.predict(x_new)
print('sum : ', np.sum(pred))

print('분류 결과  : ', pred)
print('분류 결과  : ', np.argmax(pred))
print()