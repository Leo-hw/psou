'''
연산자 
'''
#print() 문 사용 연습
from builtins import divmod
from sqlalchemy.sql.expression import false

print(format(1.5678, '10.3f')) #전체 자릿수.소숫점이하 자리수
print('나는 나이가 %d 이다.'%23) #  %d 데시말. 10진수. 기호와 1:1대응
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33)) 
print('이름은 {}, 나이는 {}'.format('신선해', 33)) # 순서를 안주면 기본적으로 적힌 순서대로.
print('이름은 {1}, 나이는 {0}'.format(34, '강나루')) # 순서를 주면 순서에 맞게.

print()
v1 = 3
v1 = v2 = v3 = 5
print(v1,v2,v3)

print('출력1', end=',') # 계속 이어서 출력 가능
print('출력2\n출력3')

# print 는 기본적으로 라인 스킵. 라인스킵을 안하고 싶을 경우 end=

v1 = 1,2,3
print(v1)
v1,v2 = 1000, 2000
print(v1,v2)
v2,v1=v1,v2
print(v1,v2)

print('값 할당용 packing')
v1,*v2=1,2,3,4,5
print(v1)
print(v2)

print('패킹 연산자')     # *을 가진 변수가, 패킹... 배열?을 가지고 나머지를 v2가 가짐.
*v1,v2=1,2,3,4,5 
print(v1)
print(v2)

*v1, v2, v3=1,2,3,4,5 #패킹 연산자는 한번에 하나만 사용 가능
print(v1)
print(v2)
print(v3)

print('연산자-------')
print(5+3,5-3,5*3,5/3,5//3,5%3,5**3)
#           8,    2,   15, 1.6666666666666667, 1, 2, 125

#나누기의 경우 몫과 나머지 얻기
print('나누기의 경우 몫과 나머지 얻기 : ' , divmod(5,3))

print(1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024*1024)
#컴퓨터의 허용범위까지 연산.
#자바와 다름.계속적으로 연산 가능.
print('우선순위 :',3+4*5,(3+4)*5)

print('관계 연산자 --------')
print(5>3, 5==3, 5!=3)
print('논리 연산자 =--------')
print(5>3 and 4>3, 5>3 or 4<3, not(5>=3))

print('문자열 더하기 ---------')
print('한'+'국'+'만세')
print('대한민국'*10)

print('\n누적 -------')
a=10
a = a+1
a+=1
#a++, a-- 
#자바의 증감연산자는 파이썬에서 사용 불가
print('a : ',a)

print('부호 변경     : ',a,' ',a*-1,-a,--a,++a )
print('bool 처리 : ', bool(True), bool(False))
print('bool 처리 : ', bool(0), bool(1.5), bool(1), bool(None), bool([]),bool({}), bool(set()))
print('bool처리 : ', bool(1), bool(-12))

print('이스케이프 문자 --------')
print('aa\tbb') # 탭 \t
print('aa\bbb') # 한칸 띄우기 \b
print('aa\nbb') # 라인스킵 \n
print('c:\abc\nbc\tbc\good.txt') # 이렇게 쓰면 라인스킵이 됨.\
print(r'c:\abc\nbc\tbc\good.txt') # r을 선행하면 \를 해석하지 않음(이스케이프 문자.)


