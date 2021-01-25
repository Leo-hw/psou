'''
여러줄 주석
또는 문자열 처리
@author: KITCOOP
'''
from builtins import isinstance
"""
여러줄 주석
"""
# 한줄 주석.
# 잘 보이나?
# 이게 더 나은 거 같

#변수
var1='안녕 파이썬' # "안녕 파이썬"
print(var1)
var1 = 5; print(var1) 
#들어오는 데이터에 따라 데이터 타입이 결정됨.
#세미콜론은 줘도 되고 안줘도 되지만 한줄에 두개의 스테이트먼트 일경우 줘야함

a = 10  # 객체의 주소 기억. - 참조형 변수/기본형X
b = 20.5
c = b   # 주소 치환
print(a,b,c)
print('주소', id(a),id(10),' ',id(b),id(20.5),' ',id(c))
# a의 주소와 10의 주소가 같고, b와 20.5 의 주소가 같음. c의 주소는 b의 주소와 치환했으므로 b, c, 20.5의 주소는 같음
print(a is b, a==b) # is 는 주소값을 비교.
print(b is c, b==c) # == 는 값을 비교.

A=1; a=2;
print('A+a :', A+a, id(A), id(a))
# 대소문자를 구분.

# for = 10     #예약어는 변수명으로 사용 불가.
import keyword
print("예약어 키워드 목록 : " , keyword.kwlist)

print(10, oct(10),hex(10),bin(10)) # 10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)

# type 확인
print(1, type(1))
print(1.2, type(1.2))
print(1+2j, type(1+2j))
print(True, type(True))
print('1', type('1'))
print()
print((1,), type(1,))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))
print()
print(isinstance(1, int)) #인스턴스 확인. isinstance
print(isinstance(1, float))


