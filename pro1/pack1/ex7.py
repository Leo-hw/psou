# for
# for target in object :
#        statement
#        ...

for i in [1,2,3,4,5]:
    print(i, end = ' ')
    
print()
#colors = ['r','g','b'] #list type - 순서 있음.
#colors = {'r','g','b'} #set type - 순서가 없음.
colors = ('r','g','b') #tuple type - 순서 있음
for v in colors:
    print(v, end = ' ')
    
print()
soft = {'java':'웹용 언어', 'python':'만능언어', 'mysql':'db처리'}
for i in soft.items():
    #print(i)
    print(i[0]+ " " + i[1])
    
print()
for k,v in soft.items():
    print(k,' ' , v)
print()
for v in soft.values():
    print(v, end = ' ')
print()

print('-------------')
for gu in [2,3]:
    print('--{}단--'.format(gu))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(gu, i, gu*i))
        
print()
#for 사용시 요소 값 뿐만 아니라 인덱스도 얻고 싶어~
li=['a','b','c']
for i, v in enumerate(li):
    print(i, v)

print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 3:
        continue
    print(i, end = ' ')
else:
    print('반복문 정상 수행시 처리됨')
    
print()
#paul park(내가 매우 좋아하는 파트너) 이 5회 시험을 본다고 할 때, 70 점 이상인 경우만 합격 처리
jumsu = [95,70,60,68,100]
number = 0
for jum in jumsu:
    number +=1
    if jum < 70: continue
    print('%d 번째 합격함'%number) 

print()
l1 = [3,4,5]
l2 = [0,5,1,2]
for a in l1:
    for b in l2:
        print(a+b, end = ' ')

print()
result = [a + b for a in l1 for b in l2]
print(result)
for d in result:
    print(d, end = ' ')
            
print('\n자료 검색 후 문자열 자르기에서 분리된 문자열  수 출력')
import re
ss= '''
LG는 최근 13경기에서 10승3패로 고공비행했다. 지난 20일 2위 경쟁팀인 KT 위즈를 7대6으로 꺾고 단독 2위 체제를 굳건히 했다. 남은 경기 상대는 KIA 타이거즈, NC 다이노스, 한화 이글스, SK 와이번스다. NC는 사실상 페넌트레이스 우승을 확정했고, 나머지 3팀은 포스트시즌 진출을 포기했다. LG를 상대로 총력전을 펼칠 이유가 적은 팀들이다. LG의 플레이오프 직행이 유력해 보이는 이유다.
'''
ss2 = re.sub(r'[^가-힣\s]','',ss) # 한글, 공백 이외의 자료는 제거
print(ss2)

ss3 = ss2.split(' ') # 공백을 구분자로 문자열 분리
print(ss3)
cou = {}  #단어의 발생횟수용 dict type
for i in ss3:
    if i in cou:
        cou[i] +=1
    else:
        cou[i] = 1
print(cou)     

print()
for test_str in ['111-1234', '일일일-일이삼사','222-1234','2222-1234']:
    if re.match(r'^\d{3}-\d{4}$', test_str):
        print(test_str, '전화번호 맞아')
    else:
        print(test_str, 'ㅠㅠ')

print('사전형 자료 ---')
from time import localtime
print(localtime())
act = {6:'잠', 9:'아침먹고 출발', 18:'공부',24:'휴식'}
print(act)
hour = localtime().tm_hour;
print('현재시간', hour)
print(sorted(act.keys()))

for act_time in sorted(act.keys()): #[6, 9, 18, 24]
    if hour < act_time:
        print(act[act_time]);
        break
    else:
        print('넌 뭐니?')

print('사전형 자료로 과일 값 계산')
price = {'사과':1000, '감':500, '배':3000}
guest = {'사과':5, '감':2} # 고객 구매 목록 
bill = sum(price[f] * guest[f] for f in guest)
print('고객이 구매한 고일 가격 총액:{}원'.format(bill))


    
print()
datas = [1,2,'a', True, 3.4]
li = [i*i for i in datas if type(i) == int]
print(li)

print()
datas = {1,1,2,2,3,1,1,2,2,3,1,1,2,2,3} # 중복 제거
se = {i*i for i in datas}
print(se)

print()
id_name = {1:'tom', 2:'james'} # k, v  교체하기
name_id={val:key for key, val in id_name.items()}
print(name_id)

print()
temp = [1,2,3,1,2,3]
for i in temp:
    print(i, end = ' ')
print()
print([i for i in temp]) #[1, 2, 3, 1, 2, 3]
print({i for i in temp}) #{1, 2, 3}

print()
temp2 = list()
print(type(temp2))
for i in temp:
    temp2.append(i+100)
print(temp2)
temp2 = [i +100 for i in temp]
print(temp2)

print()
aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a + b, end = ' ')

print('\n------- range()함수와 함께 하기 ----------')
print(list(range(1,6))) # 1~6까지
print(list(range(0,11,3))) #0에서 11까지 3마다..
print(list(range(-10,-101,-30)))
print(set(range(1,6)))
print(tuple(range(1,6)))

print()
for i in range(6):
    print(i, end = ' ')
print()
tot = 0
for i in range(1, 11):
    tot +=1
print('합은 ', str(tot))

print()
for i in range(2, 5):
    for j in range(1,10):
        print('{0}*{1}={2}'.format(i, j, i*j, end = ' '))
        print()
        
print()

# 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(1,6):
    n1 = i+1
    for j in range(1,6):
        n2 = j+1 
        n = n1 +n2
        if n % 4 == 0:
            print(n1,n2, n)
            #print('{0}+{1}={2}'.format(i, j, i+j, end = ' '))
    
#  n - gram : 문자열에서 n 개의 연속된 일부 문자를 추출하는 방법
sss = 'hello'

for i in range(len(sss)-1):     # 2-gram
    print(sss[i],sss[i +1], sep = ' ')

print()

for i in range(len(sss)-2):     # 3-gram
    print(sss[i],sss[i +1],sss[i +2], sep = ' ')
    
    
    
    
    
    