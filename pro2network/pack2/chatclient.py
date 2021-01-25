'''
멀티 채팅을 위한 클라이언트
'''

import socket
import threading
import sys

def Handler(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('utf_8'))
        
#파이썬은 표준 출력의 경우, 기본적으로 버퍼링이 됨.

sys.stdout.flush()          #현재 BUFFER 에 저장된 내용을 출력장치로 내보내고 buffer 를 비움 # 안해도 되지만 나중에 부하가 걸릴 수 있음

name = input('채팅 아이디 입력 : ')
cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
cs.connect(('192.168.0.52',5555))
cs.send(name.encode('utf_8'))

th = threading.Thread(target=Handler, args=(cs,))
th.start()

while True:
    msg = input()       # 채팅 메세지 입력.
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('utf_8'))
    
cs.close()
        





            
        
