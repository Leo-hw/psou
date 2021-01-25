#turtle 모듈을 이용해 그래픽 처리
#import turtle
# a = turtle.Pen()
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# 
# #a.reset()
# a.pencolor('blue')
# a.circle(50, 360)
# 
# a.up()
# a.forward(100)
# a.write('문자 그리기', True, 'Left', font = ('고딕',30,'normal'))
# 
# input()

from turtle import *
p=Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()