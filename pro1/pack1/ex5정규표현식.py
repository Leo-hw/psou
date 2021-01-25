'''
정규표현식
https://docs.python.org/3/library/re.html?highlight=re#module-re
-특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어.
-Programming Language나 Text Editor 등 에서 문자열의 검색과 치환을 위한 용도로 사용.
-입력한 문자열에서 특정한 조건을 표현할 경우 일반적인 조건문으로는 다소 복잡할 수도 있지만, 정규 표현식을 이용하면 매우 간단하게 표현
-코드가 간단한 만큼 가독성이 떨어져서 표현식을 숙지하지 않으면 이해하기 힘들다는 문제점 
- 파이썬에서 정규식은 re 모듈이 제공
'''
import re
from re import IGNORECASE

ss = '1234 abc가나다ABC_%%%_6_1234마바사abcabc'
print(re.findall(r'123', ss))
print(re.findall(r'가나다', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]{2,3}', ss))
print(re.findall(r'[a-zA-Z가-힣]{2,3}', ss))
print(re.findall(r'.bc', ss))
print(re.findall(r'..c', ss))
print(re.findall(r'.^1+', ss))
print(re.findall(r'[^a-zA-Z가-힣]{2,3}', ss))
print(re.findall(r'\d{1,3}',ss))

print()
m = re.match(r'[0-9]*', ss)
print(m)
print(m.group()) # match 의 결과는 group() 사용

print('---------'*10)
p = re.compile('the', re.IGNORECASE) # flag 사용
print(p.findall('The dog will be the dog of today')) #대소문자 구분 없이 출력
s = '''My name is tom
I am happy'''
print(s)
p = re.compile('^.+', re.MULTILINE)
print(p.findall(s))
