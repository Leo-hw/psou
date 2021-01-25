# constant(), Variable(), function
import tensorflow as tf
import numpy as np


a = 10
print(type(a))
b = tf.constant(10)     # Graph 객체에 포함된 멤버.
print(b, type(b))
c = tf.Variable(10)
print(c, type(c))

'''
g1 = tf.Graph()    
with g1.as_default():
    #bb = tf.constant(10)
    bb = tf.Variable(10)
    print(bb)
    print(type(bb))
    print(bb.op)
    print('--')
    print(g1.as_graph_def())
'''

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(3.0)
print(node1, node1.numpy())
print(node2, node2.numpy())

node3 = node1 + node2
print(node3)
node4 = tf.add(node1, node2)
print(node4)

print('-------------------')
v = tf.Variable(1)

@tf.function            # 이걸 달아줘야 속도가 빨라짐. auto graph  -> 함수도 그래프 영역내에서 // 하지만 처음부터 붙이고 작업하면 디버깅하면 어려움. 그래서 나중에 작업 후에 붙이는 것이 좋다.
def find_next_odd():
    v.assign(v+1)
    if tf.equal(v %2, 0):
        v.assign(v+10)
        
find_next_odd()
print(v, '  ', v.numpy())

print('-----------------------------')
def func():
    #imsi = tf.constant(0)           # imsi = 0
    imsi = tf.Variable(0)
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
        #imsi = imsi +su
        #imsi += su        # tf.Variable(0) 인 경우 얘는 안먹음.  -   이런 특성들을 알아야해.
        print(imsi)
    return imsi

kbs = func()
print(kbs.numpy(), ' ', np.array(kbs))          # 둘 다 같은 말. graph -> nd array

print('*+*+'*10)
imsi = tf.constant(0)


def func2():
    global imsi
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
    return imsi

mbc= func2()
print(mbc.numpy(), ' ', np.array(mbc))


print(' ***************** '*10)
def func3():
    imsi = tf.Variable(0)
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
    return imsi

ytn= func3()
print(ytn.numpy(), ' ', np.array(ytn))


print(' ^^^^^^^^^^^^^^ '*10)
@tf.function
def func4():
    imsi = tf.Variable(0)
    su = 1
    for _ in range(3):
        #imsi = tf.add(imsi, su)
        imsi.assign(imsi+su)
    return imsi

tvn= func4()
print(tvn.numpy(), ' ', np.array(tvn))

print('구구단 출력')
@tf.function
def gugu1(dan):
    su = 0
    for _ in range(9):
        su = tf.add(su, 1)
        print(su)
        #print(su.numpy())            # err
        #print('{}*{}={:2}'.format(dan, su, dan*su))        # err
        
gugu1(3)
    