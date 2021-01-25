'''
변수의 생존 범위 : Local > Enclosing function > Global
'''

player = '국가대표'     #전역변수 : 현재 모듈의 어디서든 참조 가능
def funcSoccer():
    name = '손흥민'
    player ='동네대표'  #지역변수
    print(name, player)
    
funcSoccer()

print('--------------')
a = 10; b = 20; c = 30;                                                             # 전역 변수(Global Variable)
print('1. a:{}, b:{}, c:{}'.format(a,b,c))

def kbs():
    a = 40                                                                                      # 지역 변수(Local Variable)
    b = 50
    def mbc():  # 내부 함수
        global c                                                                                  # 이렇게 써주는 순간 전역변수(Global Variable)가 된다.
        nonlocal b                                                                              # 한 단계 상위 함수 수준
        #c=60                                                                                    # 지역 변수(Local Variable)
        print('2. a:{}, b:{}, c:{}'.format(a,b,c))
        c=60                                                                                    # 지역 변수(Local Variable)지만 참조형 변수 - 값을 가지지 못했기 때무네 에러
        b=70
    mbc()
    a = 80
    b = 90
    c = 100
kbs()
print('3. a:{}, b:{}, c:{}'.format(a,b,c))        

print()
print()
g = 1
def func1():
    global g            # <================ *****주의 *****
    a = g
    g = 2
    return a

print(func1())

print('가아자아~' *10)
# 인수 argument 키워드로 매핑
def ShowGugu(start=1, end = 5):
    for dan in range(start, end + 1):
        print(str(dan)+'단 출력')
        
ShowGugu(2, 3)
print()
ShowGugu(3)
print()
ShowGugu()
print()
ShowGugu(start=2, end = 3)
print()
ShowGugu(end =5, start=1)
print()
ShowGugu(3, end = 5)
print()
#ShowGugu(start=3, 5) # error//SyntaxError: positional argument follows keyword argument
#ShowGugu(end=4, 3) #SyntaxError

print('가변 인수 처리 -----')
def fu1(*ar):
    print(ar)
    for i in ar:
        print('국 없이 먹는 법 : '+i)
#fu1('김밥', '비빔밥') #TypeError: fu1() takes 1 positional argument but 2 were given
fu1('김밥')
print()
fu1('김밥','주먹밥') # 튜플 타입으로 처리.
print()
fu1('김밥','주먹밥','비빔밥') 
print()

def fu2(a, *ar):
    print(a)
    print(ar)
    
fu2('김밥','비빔밥','주먹밥')

print()
# def fu3(*ar, a):
#     print(a)
#     print(ar)
#     
# fu3('김밥','비빔밥','주먹밥')

print()
def selProcess(choice, *ar):
    if choice == '+':
        re = 0
        for i in ar:
            re += i
    elif choice == '*':
        re = 1
        for i in ar:
            re *= i
    return re
        
print(selProcess('+',1,2,3,4,5))
print(selProcess('*',1,2,3,4,5))

print()
def fu4(w, *h, **other):
    print('몸무게{}, 키{}'.format(w,h))
    print(other)
#fu4(66, 160, {'irum':'지구인', 'nai':22})
fu4(66, 160,165,170, irum='지구인', nai=22)

print('\n------------- closure 들어가기 전 워밍업 ----------------')
def abc(aa, bb):
    cc = aa * bb
#    print(cc)
    return cc

print(abc(2,3))
#print(cc)        # 함수내에서만 유효하므로 error

ytn = abc
print(ytn(2,3))

del abc         # 함수명을 삭제 : 참조 객체는 메모리에 저장
#print(abc(2,3))        # NameError: name 'abc' is not defined        // 함수명 만 삭제. 인스턴스를 지우진 않음
print(ytn(2,3))
tvn = ytn
print(tvn(2,3))

print('-------------- closure 들어가기 전 워밍업 끝 ---------------')

def out():  #함수는함수를 가져
    count = 0;
    def inn():  # 이거 내부함수야.
        nonlocal count
        count += 1
        return count
    print(inn())
#print(count)    # 함수 내 참조 불가.
out()
out()

def outer():  #함수는함수를 가져
    count = 0;
    def inner():  # 이거 내부함수야.
        nonlocal count
        count += 1
        return count
    return inner # <== 이것을 클로저 라고 한다. (내부 함수를 반환)

inner_func_addr = outer()
print(inner_func_addr)
print(inner_func_addr())
print(inner_func_addr())
print(inner_func_addr())
print(inner_func_addr())
print()

inner_func_addr2 = outer()
print(inner_func_addr2())
print(inner_func_addr2())

print('수량 * 단가 * 세금 = 결과 출력하기')
def outer2(tax):
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2

r = outer2(0.1)
result1 = r(5, 10000)
print(result1)
result2 = r(10, 20000)
print(result2)

print()
r2 = outer2(0.1)
result3 = r2(5, 10000)
print(result3)

