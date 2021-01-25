'''
Process 클래스 사용: Pool 과 달리 그저 하나의 프로세스를 함수에 적당한 인자 값을 할당해주고 더 이상 신경쓰지 않는다.

'''


import os
import time
from multiprocessing import Process

def func():
    print('연속 적으로 진행할 어떤 작업')
    time.sleep(1)
    
def func2(number):
    result = number + 10
    func()
    proc = os.getpid()
    print('number:{0}, result:{1} proc id :{2}'.format(number, result, proc))
    
if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    procs= []
    
    for index, number in enumerate(numbers):
        proc = Process(target=func2, args=(number, ))
        procs.append(proc)  # join 을 위해.
        proc.start()        # func2가 호출
        
    for p in procs:
        p.join()

