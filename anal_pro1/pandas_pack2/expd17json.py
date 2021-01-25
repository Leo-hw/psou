'''
JSON
'''

import json
from nltk.util import pr

dict = {'name':'tom', 'age': 22, 'score': ['90','70','100']}
print(dict, type(dict))

print('인코딩 ---')
str_val = json.dumps(dict)          # 인코딩. (dumps 를 통해 인코딩 후 받을 수 있음)
print(str_val, type(str_val))
print(str_val[0:20])        # 문자열 관련 명령어(문자열 슬라이싱)
#print(str_val['name'])        # dict 관련 명령어이기 때문에 에러. 이미 문자열로 컨버팅 됨

print('디코딩 -----')
json_val = json.loads(str_val)
print(json_val, type(json_val))
print(json_val['name'])        # dict 관련 명령어
#print(json_val[0:20])        # 문자열 관련 명령어 이므로 에러. dict

print('^^^^'*20)
# 웹에서 json 자료 읽기
import urllib.request as req

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoullibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
print(plainText, ' ', type(plainText))      #class 'str'

jsonData = json.loads(plainText)
print(jsonData, ' ', type(jsonData))
print(jsonData['SeoullibraryTime']['row'][0]['LBRRY_NAME'])

jsonData = json.loads(plainText)

print(jsonData, ' ', type(jsonData)) # <class 'dict'>

print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])
print()

libData = jsonData.get('SeoulLibraryTime').get('row')
print(libData) # 5개 dict 타입

name = libData[0].get('LBRRY_NAME')
print(name)
print('---------------')

for ele in libData:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name + '\t' + tel + '\t' + addr)