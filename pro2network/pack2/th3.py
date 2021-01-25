'''
Thread 클래스 상속            // 스레드는 상속이 가능.
'''
import threading, time


class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            print('id:{}==>{}'.format(self.getName(), i))
            time.sleep(0.1)
            
ths = []
for i in range(1,3):
    th = MyThread()
    th.start()
    ths.append(th)

for t in ths:
    t.join()

print('프로그램 종료')
