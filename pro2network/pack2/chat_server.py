'''
멀티 채팅을 위한 서버
'''
import socket
import threading

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ss.bind(('',5555))
ss.listen(5)
print('채팅 서버 서비스 시작...')
users=[]

def ChatUser(conn):
    name = conn.recv(1024)
    data = '^^' + name.decode('utf_8') + '님 등장!'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('utf_8'))        #모든 채팅 사용자에게 입장을 알림
            
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf_8') + '님 메세지: ' + msg.decode('utf-8')
            print('수신된 글 : ', data)
                
            for p in users:
                p.send(data.encode('utf_8'))        #모든 채팅 사용자에게 글을 전송
                    
    except:         # 채팅 사용자가 채팅방을 빠져 나간 경우
        msg = conn.remove(conn)
        data = 'Adios!' + name.decode('utf_8') + '님 퇴장!'        
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode('utf_8'))    
                
    
while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=ChatUser, args = (conn,))
    th.start()
    
    
