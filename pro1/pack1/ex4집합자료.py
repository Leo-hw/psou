'''
집합형 자료 처리 - 튜플, 셀, 딕트
'''
# tuple : 리스트와 유사하나 읽기 전용
#t = ('a','b','c','a')
t='a','b','c','a'
print(t, type(t), len(t))
print('검색건수 : ', t.count('a'))
print('검색위치 : ', t.index('a'))

print()
p=(1,2,3)
print(p)
#p[1]=10 # err:'tuple' object does not support item assignment
q = list(p) # 형변환 tuple-> list 
q[1] = 10
p= tuple(q)
print(p, ' ', p[1:]) # 슬라이싱 가능

print()
t1 = (10,20)
a,b=t1
b,a = a,b
t2 = a,b
print(t2)

aa = (1)
bb=(1,)
print(type(aa), type(bb))

print('***' *20)
# set : 순서 X, 중복 불가
a = {1,2,3,1}
print(a, type(a), len(a))
b ={3,4}
print(b)
print(a.union(b)) #합집합
print(a.intersection(b)) # 교집합
print(a-b, a|b, a&b) # 차, 합 , 교 집합

#print(b[0]) # TypeError: 'set' object is not subscriptable

b.add(5) # 요소 추가
print(b)

b.update({6,7})     #set ok
b.update({8,9})     #list ok
b.update({10,11}) #tuple ok
print(b)

b.discard(7) #값에 의한 삭제
b.remove(6) #값에 의한 삭제
b.discard(7) #값이 없으면 통과
#b.remove(6)#값이 없으면 에러
print(b)

c = set()
print(type(c))
c = b
print(c)
c.clear() #요소값 모두 제거
print(c)

print('형변환 -----')
print(a)
print(tuple(a))
print(list(a))

li = [1,2,3,4]
print(li)
s = set(li)
li = list(s)
print(li)


print('******'*20)
#dict : 사전 자료형, 중복 불가 key:value 쌍으로 이루어짐, 순서 X, key 중복 X\
mydic = dict(k1=1,k2='abc',k3=3.4)
print(mydic, type(mydic), len(mydic))

dic = {'파이썬' :'뱀','자바':'커피','스프링':'용수철'}
print(dic)
print(dic['자바'])
#print(dic['커피']) #KeyError: '커피' value 값으로는 꺼낼 수 없음
dic['오라클'] = '예언자'
print(dic)

#삭제
del dic['오라클'] 
print(dic)

print(dic.keys()) # 반환 값 list
print(dic.values()) # 반환 값 list
print('자바' in dic)
print('마리아' in dic)
print(dic.get('자바'))