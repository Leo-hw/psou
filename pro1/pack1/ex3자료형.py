'''
집합형 자료처리 - 문자열, 리스트, 튜플, 셀 ,딕트
'''
# 문자열 - str


s = 'sequence'
print(len(s), s.count('e'))
print('검색위치:' , s.find('e'), s.find('e',3), s.rfind('e'))

# str 타입 객체 자료는 수정 불가 -= int, float, complex, bool, str, tuple
a = 5 # 5 140708598855584
a = 7 # 7 140708598855648
print(a, id(a))

# 5와 7 인스턴스는 각각 주소를 가지고 있고 a 는 이 주소를 참조해서 출력.

ss = 'mbc' # mbc 2356436868464
print(ss, 'mbc', id(ss), id('mbc'))

ss = 'abc' # 수정 불가능.
print(ss, 'abc', id(ss), id('abc'))

print('\n문자열은 참조만 가능하므로 수정이 불가능')
print(s) # sequence
print(s[0], s[2:4], s[:3], s[3:])
print(s[-1], s[-4:-1], s[-4:], s[::2])
#문자열 전체를 참조할 수 있지만 슬라이싱이 가능. 

print()
s2='kbs mbc'
s2 = ' '+ s2[:4]+ 'sbs ' + s2[4:] + ' '
print(s2)

print('문자열 분리 ----')
s3 = s2.split(sep=' ') # 구분자는 공백
print(s3)

print('문자열 합치기')
print(':'.join(s3)) #문자열 결합

s4 = 'life is too short'
s5 = s4.replace('life','My leg')
print(s5)

#문자열 함수...
print("\nlist type 의 집합 자료")
#List : 순서가 있고 중복 허용. 여러 종류의 값 기억이 가능, 변경 가능, 배열과 유사,
a = [1, 2, 3]
print(a, type(a))
b=[10, a, 20.5, True, '문자열', 10]
print(b, type(b), id(b))
print(b[0], ' ', b[1],' ',b[1][1])

print()
family = ['엄마','아빠', '나', '여동생']
family.append('남동생')
family.insert(0, '할아버지')
family.extend(['삼촌','조카'])
family +=['이모', '고모']
family.remove('나')
print(family, ' ', len(family), ' ', family[2])
print(family.index('남동생'))
print('엄마'in family, ' ', '나'in family) # family 안에 있을 경우  True 없을 경우 False
#append 로 추가, insert 로 삽입 가능 /append 사용시 마지막에 값 추가.
print()
aa = [1,2,3, ['a','b','c','d'], 4,5,4,5]  #중첩 리스트

aa[0] =100 # 2758081309696
aa[3][0] = 'good'
print(aa, id(aa)) # 3022934437184
print(aa[0], aa[3])
print(aa[3][:2])

# 요소 삭제.
aa.remove(4) # 값에 의한 삭제 - 인덱스 아님.
print(aa)
del aa[4] # 순서에 의한 삭제
print(aa)
aa[3].remove('c')
del aa[3][0]
print(aa)


print()
aa =[3,1,5,2,4]
aa.sort(reverse=True) # 기본적으로 ascending sort
print(aa)

# 얕은 복사 / 깊은 복사
print('얕은 복사/깊은 복사')
bb = aa
print(bb)

print()
import copy
cc = copy.deepcopy(aa)
print(cc)
print()
aa[0]=77
print(bb)
print(cc)
print(id(aa), id(bb), id(cc)) #1889503079744 1889503079744 1889503082432

#자료 구조와 관련된 얘기
print('\nList 로 stack(LIFO) 처리') #Last In First Out
sbs= [10,20,30]
sbs.append(40)
print(sbs)
sbs.pop()
print(sbs)
sbs.pop()
print(sbs)

print('\n List 로 queue (FIFO)처리')
sbs= [10,20,30]
sbs.append(40)
print(sbs)
sbs.pop(0)
print(sbs)
sbs.pop(0)
print(sbs)



