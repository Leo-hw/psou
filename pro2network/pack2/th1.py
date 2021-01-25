'''
process : 실행 중인 응용 프로그램을 말한다. process 자신만의 메모리, data stack 등을 가지며 다른 process 와는 독립적이다.
thread : 하나의 process 내에서 진행되는 하나의 실행단위를 말하며, 여러대의 thread 를 운영함으로 해서 multi tasking 의 효과를 볼 수 있다.
                여러 thread 가 process 공간의 메모리를 공유할 수 있다.
'''

#from subprocess import *

#Popen('c:/windows/system32/calc.exe')           # 응용 프로그램을 실행 후 다음 작업 계속
#Popen('c:/windows/system32/calc.exe')
#call('c:/windows/system32/calc.exe')                  # 응용 프로그램 실행 후 해당 process 가 종료될 때까지 다음 작업 대기

#Popen('ping www.google.co.kr')
#call('ping www.google.co.kr')
#print('다음 작업~~~~~~~')

# thread 처리
import threading, time

# 스레드에 의한 처리 메소드        - 메소드의 이름은 자바와 달리 고정이 아님.
def run(id):
    for i in range(1, 30):
        print('id={} ==>{}'.format(id, i))
        time.sleep(0.1)

# 스레드를 사용하지 않은 경우
#run(1)      # 순차적
#run(2)      #

# 스레드를 사용한 경우
'''
th1 = threading.Thread(target=run, args=('일', ))
th2 = threading.Thread(target=run, args=('둘', ))
th1.start() #스레드를 시작.
th2.start()

th1.join()  # 사용자 정의 스레드가 종료 될 때까지 메인 스레드 대기
th2.join()
'''
ths = []
for i in range(1,3):
    th = threading.Thread(target=run, args=(i, ))
    th.start()
    ths.append(th)
    
for t in ths:
    t.join()
print('프로그램 종료')