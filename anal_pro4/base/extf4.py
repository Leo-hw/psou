# 연산자와 함수 일부 확인 
import tensorflow as tf
import numpy as np

x = tf.constant(7)
y = 3

# tf.cond(조건, 함수1, 함수2)
result1 = tf.cond(x>y, lambda:tf.add(x,y), lambda:tf.subtract(x,y))
print(result1.numpy())

print()
f1 = lambda:tf.constant(1)
print(f1())

f2 = lambda:tf.constant(2)
a = tf.constant(3)
b = tf.constant(4)
result2 = tf.case([(tf.less(a,b), f1)], default = f2)      # if a<b return 1 else return 2
print(result2.numpy())   

print()
print(tf.equal(1,2).numpy())
print(tf.not_equal(1,2))
print(tf.less(1,2))
print(tf.greater(1,2))
print(tf.less_equal(1,2))
print(tf.greater_equal(1,2))

print()
print(tf.logical_and(True, False).numpy())
print(tf.logical_or(True, False).numpy())
print(tf.logical_not(True))

print()
ar = [[1,2],[3,4]]
print(tf.reduce_mean(ar).numpy())
print(tf.reduce_mean(ar, axis = 0).numpy())
print(tf.reduce_mean(ar, axis = 1).numpy())

print()
t = np.array([[[0,1,2], [3,4,5]],[[6,7,8], [9,10,11]]])
print(t.shape)
print(tf.reshape(t, shape=[2,6]))
print(tf.reshape(t, shape=[-1,6]))      # -1 은 자동
print(tf.reshape(t, shape=[2, -1]))
# tensor board - 그래프 내의 텐서가 진행되는 과정을 보여주는 거.

print()
print(tf.squeeze(t))        # 차원 축소 함수 ( 열 요소수가 1개인 경우만 해당)
print()
# 텐서플로우는 차원에 민감하기 때문에 차원을 잘 다뤄야함.
aa = np.array([[1],[2],[3],[4]])
print(aa.shape)
bb = tf.squeeze(aa)
print(bb.shape)

print()
tarr = tf.constant([[1,2,3],[4,5,6]])
print(tarr.shape)
print('-----------------------------------------------------------------------------')
sbs = tf.expand_dims(tarr, 0)       # 1 번째 차원을 추가해서 확장
print(sbs.numpy(), sbs.shape)
print()
sbs = tf.expand_dims(tarr, 1)       # 2 번째 차원을 추가해서 확장
print(sbs.numpy(), sbs.shape)
print()
sbs = tf.expand_dims(tarr, 2)       # 3 번째 차원을 추가해서 확장
print(sbs.numpy(), sbs.shape)
print()
sbs = tf.expand_dims(tarr, -1)       # -1 번째 차원을 추가해서 확장
print(sbs.numpy(), sbs.shape)
