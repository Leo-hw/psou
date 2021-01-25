'''
모듈(module)의 멤버 중
     함수(function)
= 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위.

코드 관리가 효과적 
프로그램을 논리적으로 구성할 수 있다.
내장 함수와 사용자 정의 함수로 구분
'''

# 내장함수 : python 또는 제3자(Third party)가 지원하는 함수
print(sum([3,5,7]), sum((3,5,6)))
print(int(1.7), float(3), str(5)+'오')

a = 10
b = eval('a+5')
print(b)

print(round(1.2),round(1.6))
import math

print(math.ceil(1.2), math.ceil(1.6))          #근사치 중 큰 수
print(math.floor(1.2), math.floor(1.6))     #근사치 중 작은 수

b_list = [True, False]
print(all(b_list))      # 모두 참일 때 참
print(any(b_list))    # 하나라도 참일 때 참

b_list = [1,3,2,5,9,6]
res = all(a < 10 for a in b_list)
print('모든 숫자가 10미만이야?????????', res)

res = any(a < 3 for a in b_list)
print('숫자 중에서 3미만이 있느냐?', res)

print()
c_list = ['가나다', '가나', '초콜릿', '가나다초콜릿', '가나초콜릿', '가나 초콜릿']
res = any(a =='초콜릿' for a in b_list)
print('문자 중에서 초콜릿 있느냐?', res)

x= [10,20,30]
y = ['a','b']
for i in zip(x,y):
    print(i)
#(10, 'a')
#(20, 'a')

# ...

print('\n\n 사용자 정의 함수 ------------')
def Dofunc1():
    print('Dofunc1()')
def dofunc2(name):
    print('안녕 ~', name + '님')

Dofunc1()
print('딴짓 하다가')
Dofunc1()
print('함수명은 함수 객체의 주소를 기억: ', Dofunc1)
print(type(Dofunc1))
dofunc2('paul')
print(dofunc2('paul park'))


print()
def doFunc3(arg1, arg2):
    c = arg1 + arg2
    if c % 2 ==1:
        return 
    else:
        return c
    
print(doFunc3(10, 2))
print(doFunc3(10, 3))

print(dir(__builtins__))
print(globals())
OtherFunc1 = Dofunc1        # 주소를 치환
OtherFunc2 = Dofunc1()    # 실행결과를 치환
# 차이점을 알아둬야만 한다.
OtherFunc1()
OtherFunc2

print()
def swap(a,b):
    return b, a 
#return이 복수 개일 경우 tuple 로 리턴
print(swap(10,20))

print()
def isOdd(arg):
    return arg % 2 == 1

print(isOdd(5))
print(isOdd(6))

myDict = {x:x*x for x in range(11) if isOdd(x)} # 조건에 함수 적용
print(myDict)
