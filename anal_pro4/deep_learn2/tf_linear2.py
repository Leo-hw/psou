import tensorflow as tf
import numpy as np

# 선형 회귀 모델 계산으로 작성
opti  = tf.keras.optimizers.SGD()

w = tf.Variable(tf.random.normal((1,)))
b = tf.Variable(tf.random.normal((1, )))

@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        hypo = tf.add(tf.multiply(w, x), b)
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo,  y)))
    grad = tape.gradient(loss, [w,b])
    opti.apply_gradients(zip(grad, [w,b]))
    return loss

x = [1., 2., 3., 4., 5.]        # feature
y = [1.2, 2.0, 3.0, 3.5, 5.5]       # label

w_vals = []
loss_vals = []

for i in range(100):
    loss_val = train_step(x, y)
    loss_vals.append(loss_val.numpy())
    w_vals.append(w.numpy())
    if i  % 10 == 0 :
        print(loss_val)

print(loss_vals)
print(w_vals)
    
import matplotlib.pyplot as plt
plt.plot(w_vals, loss_vals, 'o')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()    

y_pred = tf.multiply(x, w) +b
print(y_pred.numpy())

plt.plot(x, y, 'ro')
plt.plot(x, y_pred, 'b-')
plt.show()
