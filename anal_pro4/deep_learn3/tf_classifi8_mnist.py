# MNIST dataset : 손글씨 이미지 분류

import tensorflow as tf
import sys

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
#print(x_test, x_test.shape, '  ', y_train.shape)    #  (10000, 28, 28)    (60000,)
#print(y_test, y_test.shape)        # (10000,)
'''
print(x_train[0])
for i in x_train[0]:
    for j in i:
        sys.stdout.write('%s  %j')
    sys.stdout.write('\n')
'''
'''
# 이미지로 보기
import matplotlib.pyplot as plt
plt.imshow(x_train[0].reshape(28,28), cmap='Greys') 
plt.show()
'''
print(y_train[0])       #5

# 모델에 적용하기 위해 
x_train = x_train.reshape(60000, 784).astype('float32') 
x_test = x_test.reshape(10000, 784).astype('float32')
print(x_train[0])
print()
x_train /= 255  # 0~1 사이로 정규화        // 정규화를 시킬 경우 분류 정확도가 높아짐 
x_test /= 255   
print(x_train[0])

print('레이블의 종류 : ',  set(y_train))  #레이블의 종류 :  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# label 자료에 대해 One_hot encoding 
y_train = tf.keras.utils.to_categorical(y_train, 10)        # np에도 있음
y_test = tf.keras.utils.to_categorical(y_test, 10)        
print(y_train[0])

# train data의 일부를 validation data 로 분리하기
x_val= x_train[50000:60000]
y_val= y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
print(x_val.shape, x_train.shape)   #(10000, 784) (50000, 784)
"""
#model 
model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(512, input_shape=(784, )))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))     # 과적합 방지를 위해 20% 정도는 학습에서 제외( 보통 0.5를 넘기지 않음)

#regularizers.l2 (0.001) -  가중치 행렬의 모든 원소를 제곱하고 0.001을 곱하여 네트워크의 전체 손실에 더해진다는 의미, 이 규제(패널티)는 훈련할 때만 추가됨
model.add(tf.keras.layers.Dense(512, kernel_regularizer=tf.keras.regularizers.l2(0.001)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2))     

model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(patience=5)          # 5개 비슷할 경우 조기 종료한다는 말

history = model.fit(x_train, y_train, epochs=1000, batch_size=128, \
                    validation_data=(x_val, y_val), verbose=2, callbacks = [early_stop])
print(history.history.keys())
print(('loss:', history.history['loss']))
print(('val_loss:', history.history['val_loss']))
print(('accuracy:', history.history['accuracy']))
print(('val_accuracy:', history.history['val_accuracy']))

# 시각화 
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label = 'loss')
plt.plot(history.history['val_loss'], label = 'val_loss')

plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

# 모델 평가 
score = model.evaluate(x_test, y_test, batch_size = 128, verbose=2)
print('evaluate loss : ', score[0])
print('evaluate acc : ', score[1])
"""
import matplotlib.pyplot as plt
# 모델 저장 및 읽기
#model.save('mnist_model.hdf5')
model = tf.keras.models.load_model('mnist_model.hdf5')

# ------------------------------
# 1. 기존 자료로 예측
print(x_test[:1], x_test[:1].shape)
plt.imshow(x_test[:1].reshape(28, 28), cmap = 'Greys')
plt.show()

import numpy as np
pred = model.predict(x_test[:1])
print('예측값 : ', np.argmax(pred,1))
print('실제값 : ', np.argmax(y_test[:1]))      # y_test 는 one_hot_encoding 되어 있으므로 배열 중 가장 큰 값을 보여주는 argmax를 사용

# 내가 그린 이미지 분류 결과 확인
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('nike.png')
img = np.array(im.resize((28,28), Image.ANTIALIAS).convert('L'))
print(img, img.shape)

data = img.reshape([1,784])
#print(data)
data = data / 255.0
#print(data)

plt.imshow(data.reshape(28,28), cmap = 'Greys')
plt.show()

new_pred = model.predict(data[:1])
print('분류 예측 결과 : ', np.argmax(new_pred,1))
