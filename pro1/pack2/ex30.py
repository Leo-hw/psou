# file i/o

import os
print(os.getcwd())


try:
    print('file 읽기')
    #f1 = open('C:/work/psou/pro1/pack2/ftest', encoding='utf-8')
    f1 = open(os.getcwd()+'\\ftest', encoding='utf-8')
    #f1 = open('/ftest', mode='r', encoding='utf-8')
    print(f1)
    print(f1.read())
    f1.close()
    
    
    print('file 저장')
    f2 = open('ftest2.txt', mode = 'w', encoding='utf-8')           # 모드에서 파일에 대한 상태 결정.  w = write/ a = append/ r = read
    f2.write('My friend\n')
    f2.write('홍길동, 신기해')
    f2.close()
    print('저장성공')
    
    print('file 추가')
    f3 = open('ftest2.txt', mode = 'a', encoding='utf-8')
    f3.write('\n손오공')
    f3.write('\n저팔계')
    f3.write('\n사오정')
    f3.close()
    
    print('file 읽기2---------------------- ')
    f4 = open('ftest2.txt', mode = 'r', encoding='utf-8')
#    print(f4.read())
    #print(f4.readline())        # 1행 씩 읽기
    #print(f4.readline())
    
    lines = f4.readlines()          # 모든 행이 읽혀서 변수가 기억 
    print(lines)
    print(lines[0])
    print(lines[1:5])
    f4.close()
    
except Exception as e:
    print('err : ' + e)

print('^^'*20)

try:
    #파일저장
    with open('ftest3.txt', mode = 'w', encoding='utf-8') as f1:
        f1.write('파이썬으로 문서 작성 후 저장\n')
        f1.write('with open하면 \n')
        f1.write('자동으로 close() 수행 됨')
    print('저장완료')
    
    #파일읽기
    with open('ftest3.txt', mode = 'r', encoding='utf-8') as f2:
        print(f2.read())
    
    
except Exception as e2:
    print('err : ' + e2)

print('\n\n피클링(복합 객체 처리)- object type 으로 파일 i/o')
import pickle

try:
    dictData = {'tom':'111-1111', 'james':'222-2222'}
    listData = ['마우스', '키보드']
    tupleData = (dictData, listData)            # 복합 객체
    
    with open('fpickle.dat', 'wb') as f3:
        pickle.dump(tupleData, f3) #복합 객체 저장 - 저장(대상, 파일 객체명)
        pickle.dump(listData, f3)   # 리스트 객체 만 저장
    print('pickle 을 이용한 저장 완료')
    
    with open('fpickle.dat', 'rb') as f4:
        a, b = pickle.load(f4)
        print(a)
        print(b)
        c = pickle.load(f4)
        print(c)
    
except Exception as e3:
    print('err : ' + e3)


print('동 이름으로 우편번호 찾기, 나머지 주소 찾기---------------------------------------------------------')
try:
    dong = input('동이름 입력 :')
    #dong = '역삼'
    #print(dong)
    
    with open(r'zipcode.txt', mode = 'r', encoding = 'euc-kr')as zipf:
        line = zipf.readline()
        #print(line)
        while line:
            #lines = line.split('\t')
            lines = line.split(chr(9))
            #print(lines)
            #break
            if lines[3].startswith(dong):
                #print(lines)
                print('['+lines[0]+']'+' '+\
                      lines[1]+' '+ lines[2]+' '+ lines[3]+' '+ lines[4])
            
            line = zipf.readline()
            
        
    
except Exception as err:
    print('err : ' , err)
    



