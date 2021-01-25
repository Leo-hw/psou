# IMDB (영화 리뷰 관련 자료 데이터베이스) / 긍정:부정 = 5:5

from tensorflow.keras.datasets import imdb

(train_data, train_label), (test_data, test_label) = imdb.load_data(num_words = 10000)


print(train_data)
print(train_label)

aa = []

for seq in train_data:
    print(max(seq))
    aa.append(max(seq))
    print(max(aa), len(aa))
    
    
word_index = imdb.get_word_index()      # word_index 는 단어와 정수 인덱스를 매핑한 dict
rever_word_index = dict([(value, key) for (key, value) in word_index.items()])
print(rever_word_index) 
decord_review = ' '.join([rever_word_index.get(i-3, '?') for i in train_data[0]])
print(decord_review)

# list type 의 자료를 Tensor 로 변환. One-hot encoding
import numpy as np

def vector_seq(sequences, dim = 10000):
    results = np.zeros((len(sequences), dim))
    for i, seq in enumerate(sequences):
        results[i, seq] = 1
    return results

x_train = vector_seq(train_data)
x_test = vector_seq(test_data)
print(train_data[:1])
print(x_train[:1], ' ', x_train.shape)
y_train = train_label
y_test = test_label

print()
# Model
from tensorflow.keras import models
from tensorflow.keras import layers

model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape= (10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
print(model.summary())

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
print(len(x_val), len(partial_x_train))
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train, partial_y_train, validation_data=(x_val, y_val),
                    epochs=10, batch_size=512)

print('evaluate : ', model.evaluate(x_test, y_test))

print('predict : ', model.predict(x_test[:5]))
print('predict : ', np.where(model.predict(x_test[:5]) > 0.5, 1, 0).flatten())


# 시각화

import matplotlib.pyplot as plt
history_dict = history.history

acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo"는 "파란색 점"입니다
plt.plot(epochs, loss, 'bo', label='Training loss')
# b는 "파란 실선"입니다
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()



plt.clf()   # 그림을 초기화합니다
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


# 최적화 : 모델을 학습시켜 최적의 모델 생성( 정확도)
# 일반화 : 새로운 데이터에 대한 예측 결과가 일반적인 결과로 받아들여져야 한다.
# 위 두가지를 모두 만족하려면 과적합 방지가 중요.
# train/test 분리, k-fold 모델의 parameter 수를 조정, 가중치 규제(L1, L2), Dropout, train data 수 조절...
