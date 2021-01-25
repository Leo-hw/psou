# CNN : 이미지의 특징을 뽑아 크기를 줄이고, 이를 일차원 배열로 만들어 완전 연결층( 여러 층의 Dense) 로 전달해 이미지(텍스트)를 분류
# Keras 를 이용한 레이어 구성 : Subclassing API 사용
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras import Model, datasets

# -- Data 를 골고루 섞어주기 위해  tf.data.Dataset.from_tensor_slices 사용 연습 ----------
import numpy as np
x = np.random.sample((5,2))
print(x)
#dset= tf.data.Dataset.from_tensor_slices(x)         # 입력 파이프라인을 사용가능한 객체 생성
#print('dset : ', dset)
dset= tf.data.Dataset.from_tensor_slices(x).shuffle(10000).batch(3)         # 편향된 데이터를 셔플 가능.  batch 2,3,5 ...
print('dset : ', dset)
for a in dset:
    print(a)

#-------------------------------------------------------------------------------------------------------------
print()

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
print(train_images.shape, type(train_images), train_images.ndim)        # (60000, 28, 28) <class 'numpy.ndarray'> 3
# CNN 처리를 위해 3차원 자료를 4차원으로 구조 변경. channel 을 추가(흑백: 1, 컬러: 3)
train_images = train_images.reshape((60000, 28, 28, 1))
print(train_images.shape)
train_images = train_images / 255.0        # 정규화
test_images = test_images.reshape((10000, 28, 28, 1)) 
test_images = test_images / 255.0   # 정규화

# train dataset 섞어 주기
train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).shuffle(60000).batch(28)
test_ds = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(28)
print(train_ds)
print(test_ds)

# Subclassing 모델 만들기
class MyModel(Model):       # 모델을 상속받아 사용
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(filters=32, kernel_size=[3,3], padding = 'same', activation = 'relu')
        self.pool1 = MaxPool2D((2,2))    
        self.conv2 = Conv2D(filters=32, kernel_size=[3,3], padding = 'same', activation = 'relu')
        self.pool2 = MaxPool2D((2,2))
        self.flatten = Flatten(dtype='float32')    
        self.d1 = Dense(64, activation='relu')
        self.drop1 = Dropout(rate=0.3)
        self.d2 = Dense(10, activation = 'softmax')
        
    def call(self, inputs):     # init에서 선언된 layer들을 불러와  network 구성
        net = self.conv1(inputs)
        net = self.pool1(inputs)        # 여기서 이미지맵 +1
        net = self.conv2(inputs)
        net = self.pool2(inputs)        # 여기서 이미지맵 +1
        net = self.flatten(net)
        net = self.d1(net)
        net = self.drop1(net)
        net = self.d2(net)
        return net
        
model = MyModel()
temp_inputs = tf.keras.Input(shape = (28,28, 1))
model(temp_inputs)
print(model.summary())

# loss, optimizer 객체 선언
loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()

# 일반적인 모델 학습
model.compile(optimizer = optimizer, loss =loss_object, metrics=['acc'])
model.fit(train_images, train_labels, batch_size=128, epochs=5, verbose=2, \
          max_queue_size=10, workers = 4, use_multiprocessing=True)
score = model.evaluate(test_images, test_labels)
print('test loss : ', score[0] )
print('test acc : ', score[1] )

import numpy as np
print('예측 값 : ', np.argmax(model.predict(test_images[:2]), 1))
print('실제 값 : ', test_labels[:2])

