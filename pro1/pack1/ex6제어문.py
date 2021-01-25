'''
제어문 중 if
'''
var=1               # 제어문에 의해 수행되는 명령문 들은 불럭화: 띄어쓰기
if var >= 3:
    print('크구나')
    print('참일 때 수행')
else:
    print('거짓이면 수행')
print('end if 1')

print()
jumsu = 86
if jumsu >= 90:
    print('성적우수')
elif jumsu >=70:
    print('보통')
    print('중간만 가자')
else:
    print('성적저조')
print('end if 2')

print()
# jum = int(input('점수 입력 : ')) # 형변환 int(),str()
# if 90 <= jum <= 100:
#     grade = '와우'
# elif 70 <= jum < 90:
#     grade='흠' 
# else:
#     grade='헉' 
# print(grade)    
# print('end if 3')

names=['홍길동','신기해','이겨라']
if '홍길동'in names:
    print('내 친구')
else:
    print('누구니?')
print('end if 4')

print()
a = 'kbs'
b = 9 if a == 'kbs' else 11
print(b)

a = 11
b = 'mbc' if a==9 else 'kbs'
print(b)

print()
a = 3
if a> 5:
    result= a*2
else:
    result=a+2
print(result)

print()
result=a*2 if a>5 else a+2; print(result)

a=3
print((a+2, a*2)[a>5])
# 결과가 참이면 1을 반환/ 거짓이면 0을 반환

print('\n\nwhile 문------------')
a = 1
while a<=5:
    print(a, end = ' ')
    a += 1

print()    
i = 1
while i<=3:
    j=1
    while j<=4:
        print('i:' + str(i)+" / j:" + str(j))
        j = j+1
    i=i+1

print('1~100 까지 정수 중 3의 배수의 합')
i = 1; hap = 0
while i<=100:
    if i%3==0:
        hap+=i
    i+=1
print('합은' +str(hap))
print()
colors = ['red', 'greeen', 'blue']

a = 0
while a <len(colors):
    print(colors[a], end = ' ')
    a +=1

print()
# import time
# sw = input('폭탄 스위치를 누를까요????\n[Y/N]')
# if sw == 'Y' or sw =='y':
#     count=5
#     while 1<= count:
#         print('%d초 남았어요!'%count)
#         time.sleep(1)
#         count -=1
#     print('폭발!!!')
# elif sw =='N' or sw=='n':
#     print('작업 취소')
# else:
#     print('Y 또는 N을 눌러야만 합니다.')
    
a = 0
while a <10:
    a +=1
    if a ==5: continue
    if a ==7: break
    print(a)
else:
    print('while문 정상 수행/ while 문 정상적으로 수행 한 후 빠져 나오면서 else 문 수행')
print('while 수행후 a :%d'%a)

import random
num = random.randint(1,10)
#print(num)
while 1:
    print('1~10 사이의 컴이 가진 예상 숫자 입력 : ')
    guess=input()
    su = int(guess)
    if su == num:
        print('성공 ~~~`'*5)
        break
    elif su < num:
        print('더 큰 수 입력')
    elif su >num:
        print('더 작은 수 입력')
        