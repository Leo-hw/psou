# 일급 함수 : 함수 안에 함수 선언 가능, 인자로 함수 전달, 반환 값이 함수 
def func1(a, b):
    return a + b

func2 = func1
print(func2(3,4))

print()
def func3(func):            # 인자로 함수 전달
    def func4():                # 함수 안에 함수 선언
        print('난 내부 함수야~~~')
    func4()
    return func                 # 반환 값이 함수

jtbc = func3(func1)
print(jtbc(3,4))

print('\n축약함수(lambda) - 이름이 없는 한 줄 짜리 함수 ')
def hap(x, y):
    return x + y
print(hap(2, 3))

# 위 코드를 람다로 표현
print((lambda x, y:x+y)(2,3))
gg = lambda x, y :x*y
print(gg(2,3))

# 람다도 가변인수를 사용 할 수 있다.
kbs = lambda a, su=10: a+su
print(kbs(5))
print(kbs(5,20))

print()
sbs = lambda a, *tu, **di:print(a,tu,di)
sbs(1,2,3, m = 4, n = 5)

print()
li = [lambda a, b:a+b,lambda a, b:a*b]
print(li)
print(li[0](3,4))
print(li[1](3,4))

print('\n 다른 함수에 요소로 람다 사용')
#filter(함수, 순차자료형)
print(list(filter(lambda a:a <5, range(10))))       # 0~9 사이의 정수 중 5 미만인 자료만 걸러냄
print(list(filter(lambda a:a %2, range(10))))      # 홀수만 찍힘. (0이 false 이므로 2로 나눴을 때 나머지가 나오는 게 true)

print('\n장식자(meta 기능이 있음) 사용 : 장식자는 함수를 감싸는 기능')
def make2(fn):
    return lambda:'안녕' + fn()
def make1(fn):
    return lambda:'반가워' +fn()
def hello():
    return '홍길동'

hi = make2(make1(hello))
print(hi())

print()

@make2
@make1
def hello2():
    return '신기해'

print(hello2())

print('\n 재귀 함수 :함수가 자신을 호출')
def CountDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        CountDown(n - 1) #  재귀 호출
        
CountDown(5)

print()
def totFunc(su):
    if su == 1:
        print('탈출')
        return True
    return su + totFunc(su-1)

result = totFunc(10)
print('10까지의 합은', result)
