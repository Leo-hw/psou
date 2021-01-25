'''
thread 로 날짜 및 시간 출력
'''
import time
now = time.localtime()
print('현재는 {}년 {}월 {}일{}시{}분{}초'.format(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec))
print('오늘 요일은 %d'%(now.tm_wday))        # 월요일 0...
print('오늘은 몇 번째 날 %d'%(now.tm_yday))        # 1월 1일  = 1         # 며칠 지났는지 확인.

import threading
def calendar_show():
    now = time.localtime()
    print('현재는 {}년 {}월 {}일\n{}시{}분{}초'.format(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec))
    
    
def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 41: break
        calendar_show()
        time.sleep(1)
        
th = threading.Thread(target = myRun())
th.start()

th.join()           # 사용자 정의 스레드가 종료 될 때까지 메인 스레드 작업을 멈춤.
print('프로그램 종료')
