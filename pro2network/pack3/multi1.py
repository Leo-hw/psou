'''
Thread는 GIL(Global Interpreter Lock) 을 따르고 있다. 진정한 스레드의 기능이 구사되지 못함.
multiprocess 를 통해 이러한 문제를 해결하고 있다.
multiprocessing 은 비동기적이고, 부분 작업의 활동이 비결정적(무작위/예측불가 한 경우)인 경우에 효과적!!!
'''

# Pool 클래스 : 입력값에 대해 process들을 건너건너 분배하며 unit을 실행 , 병렬화
from multiprocessing import Pool
import time
import os


def func(x):
    print('값', x, '에 대한 pid : ', os.getpid()) # 현재 실행되는 process의 id를 출력
    time.sleep(1)
    return x * x

#func(5)

if __name__ == '__main__':
    startTime = int(time.time())    # 처리 수행 시간 체크 용
    
    '''
    for i in range(0, 10):      #방법 1 )  일반적인 방법으로 함수를 호출
        print(func(i))              # 총 작업시간 : 10초
    ''' 
    # 방법 2) 멀티 태스킹이 가능한 Pool 객체로 함수를 호출
    p = Pool(12)                                                 # process 갯수를 기술(3~5개가 권장)     
    print(p.map(func, range(0,10)))         # 함수와 인자 값을 매핑하면서 처리
    endTime = int(time.time())
    
    print('총 작업시간 : ', (endTime-startTime))
    
    