# Pandas 모듈 : 고 수준의 자료 구조를 지원(Series, DataFrame)

from pandas import Series           # 인덱싱 된 1차원 배열 형태
import numpy as np


obj = Series([3,7,-5,4])
#obj = Series((3,7,-5,4))
#obj = Series({3,7,-5,4})        #set 타입은 불가능... 순서가 없어서 slicing 이 안되기 때문에

print(obj, type(obj))           # 자동으로 인덱스가 부여(명시적)

obj2 = Series([3,7,-5,4], index=['a','b','c','d'])          # 색인을 직접 지정
print(obj2)

print(obj2.sum(), sum(obj2), np.sum(obj2))
# pandas / python /numpy

# panadas 에서는 내장된 numpy 함수를 그대로 사용.
print(obj2.mean(), obj2.std(), obj2.sum())

print(obj2.values)          # 배열 값 반환
print(obj2.index)           # 인덱스 명 반환

# 슬라이싱 가능.
print('\n슬라이싱 가능------')
print(obj2[['a']], ',', obj2['a'])           # 3 , a 3           
print()
print(obj2['a':'c'], '\n', obj2[['a','b']])
print()
print(obj2[2])      # 여전히 순서도 가능
print(obj2[1:4])
print(obj2[[2,1]])
print(obj2 > 0)
print('a' in obj2)
print('kbs' in obj2)

print('\n dict type 으로 Series 객체 생성')
names = {'mouse':5000, 'keyboard':25000, 'monitor':450000}
print(names)

obj3 = Series(names)
print(obj3, ' ', type(obj3))
obj3.index = ['마우스', '키보드', ' 모니터']
print(obj3)
print(obj3[0], '  ', obj3['마우스'])

obj3.name = '상품가격'          # Series 객체에 이름 부여
print(obj3)

print('****' *10)
# DataFrame : 여러개의 Series 객체가 합쳐진 형태 / 각 칼럼은 다른 종류의 값을 기억 가능

from pandas import DataFrame

df = DataFrame(obj3)        # Series 객체를 사용해서 DataFrame 객체를 생성.
print(df, type(df))

# dict type 으로 DataFrame 생성
data = {
    'irum': ['신기해','홍길동', '강나루','공기밥','김밥'],
    'juso': ('역삼동', '역삼동', '서초동', '신사동', '서초동'),
    'nai':['22','25','32','28','22'],
    }               # set type 은 사용 불가능/ 마지막 , (comma) 는 줘도 되고 안줘도 됨
print(type(data))
print()
frame = DataFrame(data)
print(type(frame))
print(frame)

print(frame['irum'])        # 사전 형식으로 자료 읽기
print(frame.irum)        # 속성 형식으로 자료 읽기

print(type(frame.irum))     #<class 'pandas.core.series.Series'>
print()
print(DataFrame(data, columns=['juso','irum','nai']))           # 순서 변경 후 객체 생성

print() 
# 새로운 컬럼 추가 (NaN), 인덱스 명 추가
frame2 = DataFrame(data,columns=['irum','juso','nai','tel'], index=['a','b','c','d','e'])
print(frame2)

frame2['tel']='111-1111'            # 컬럼에 값을 주면, 모든 행에 적용
print(frame2)

val = Series(['222-2222','333-3333','444-4444'], index=['b','c','d'])
frame2['tel'] = val
print(frame2)

print()
print(frame2.T)     # transpose 행과 열을 바꿔줌
print()
print(frame2.values, type(frame2.values))           # 반환 타입이 'numpy.ndarray

print(frame2.values[0,1])   #역삼동
print(frame2.values[0:2])  

print(type(obj2), type(obj2.values))            
print()     # 행  열 삭제
frame3 = frame2.drop('d')           # 행 삭제 r 기본 axis=0
#frame3 = frame2.drop('d', axis=0)
print(frame3)

frame4 = frame2.drop('tel', axis=1)
print(frame4)

print()     # 정렬
print(frame2.sort_index(axis=0))                                         # 행 기준     -     오름 차순
print(frame2.sort_index(axis=0, ascending=False))       #행 기준     -     내림차순

print(frame2.sort_index(axis=1))                                         # 열 기준    -     오름차순
print(frame2.sort_index(axis=1, ascending=False))       # 열 기준     -     내림차순

print()    
print(frame2.rank(axis=0))

print()
counts = frame2['juso'].value_counts()
print('건수 : ', counts)

print()
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23,25,15],
    }

frame = DataFrame(data)
print(frame, type(frame))

#문자열 자르기
results = Series([x.split()[0] for x in frame.juso])
#results2 = Series([x.split()[1] for x in frame.juso])
results2 = Series((x.split()[1] for x in frame.juso))
#results2 = Series(x.split()[1] for x in frame.juso)
print(results, '  ' ,results.value_counts())
print()
print(results2, '  ',results2.value_counts())

