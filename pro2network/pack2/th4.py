'''
스레드 간 공유자원 값 충돌 방지 - 동기화(순서화)

'''
import threading, time

g_count = 0 # 전역 변수는 자동으로 스레드의 공유자원
lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire()      # 충돌(경쟁) 방지 목적으로 임의의 스레드가 공유자원 점유시 다른 스레드는 대기.
        print('id%s ==> count:%s, g_count:%s'%(id, i, g_count))
        g_count += 1
        lock.release()       #lock 해제    // lock 해제를 안할 경우 충돌 후 대기 상태.
        
for i in range(1,5):        # 5개의 스레드를 생성 후 특정 함수 호출
    threading.Thread(target=threadCount, args =(i, 5)).start()
    
time.sleep(1)

print('final g_count : ', g_count)
print('The end')
