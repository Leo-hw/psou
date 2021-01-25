# 일반 텍스트 파일(dict type 모양을 갖춤)을 읽어 dict type 으로 처리하기

import ast
with open('abc.txt', 'r') as f1:            #방법 1
    aa = eval(f1.read())            # 보안에 취약
    print(aa)
    print(type(aa))     #<class 'dict'>

print()
with open('abc.txt', 'r') as f2:            #방법 2
    bb = f2.read()
    print(bb)
    print(type(bb))     #<class 'str'>
    
    cc = ast.literal_eval(bb)                   #방법 3      
    #str type 을 dict type 으로 변환, eval() 보다 안전을 보장.(보안에 조금 더 유리)
    print(cc)
    print(type(cc))     #<class 'dict'>
    
    