#pandas 로 파일 읽기

import pandas as pd

df = pd.read_csv('C:/work/psou/anal_pro1/pandas_pack/testdata/ex1.csv')         
print(df, '  ', type(df))

print()
# sep / separator 가 없을 경우 , 로 구분되어있는 파일 => string으로 읽기 때문
# skipinitialspace = 공백을 제거
df = pd.read_table('C:/work/psou/anal_pro1/pandas_pack/testdata/ex1.csv', sep=',' , skipinitialspace = True)   
print(df, '  ', type(df))

print()
#칼럼 명이 없는 경우
df = pd.read_csv('C:/work/psou/anal_pro1/pandas_pack/testdata/ex2.csv', header= None)            
print(df)

print()
#칼럼 명이 없을 때, 뒤에서부터 채워줌.
df = pd.read_csv('C:/work/psou/anal_pro1/pandas_pack/testdata/ex2.csv', header= None, names=['a','b'])                  
print(df)

print()
#칼럼 명이 없을 때, 뒤에서부터 채워줌.
df = pd.read_csv('C:/work/psou/anal_pro1/pandas_pack/testdata/ex2.csv', header= None, names=['a','b','c','d','e'])                  
print(df)

#임의의 칼럼명을 인덱스 명으로 사용하고 싶을 때
print()
df = pd.read_csv('C:/work/psou/anal_pro1/pandas_pack/testdata/ex2.csv', header= None, names=['a','b','c','d','msg'], index_col='msg')                  
print(df)

# 정규 표현식 사용
# list 사용 가능시 대부분 tuple 도 사용가능. (하지만 함수에 따라 return  값이 다르므로 확인 필요)
print()
df = pd.read_table('testdata/ex3.txt', sep='\s+', skiprows=[1,3])                  
print(df)

#
print()
df = pd.read_fwf('testdata/data_fwt.txt', widths=(10,3,5), names=('date','name','price'), encoding='utf8')
print(df)
print(df['date'])
print(df.iloc[:3,2])

#chunk 단위로 데이터 읽기 : 많은 양의 자료를 원하는 크기 만큼 할당/해제하는 기능을 할 수 있다.
#<pandas.io.parsers.TextFileReader object at 0x00000260EEF8CA30>
# TextParser 객체 반환
test = pd.read_csv('testdata/data_csv2.csv', header = None, chunksize =3)
print(test)

for piece in test:
    #print(piece)
    print(piece.sort_values(by=2, ascending=True))


