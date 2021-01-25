import socket
import sys

HOST = '192.168.0.72'
HOST = ''               #현재 수행중인 컴퓨터의 IP 를 자동으로 인지, 동적.
PORT  = 7788

# SOCKET
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 종류, 유형

try:
    serverSock.bind((HOST,PORT))
    serverSock.listen(5)
    print('server start ...')
    
    while True:
        conn, addr = serverSock.accept()        # 연결 대기 - 수동적으로 대기
        print('client info : ', addr[0], addr[1])       # ip, port 
        print('수신 정보 : ', conn.recv(1024).decode())
        
        # 서버가 클라이언트에게 자료 전송
        conn.send(('from sever : ' +  str(addr[1]) + '행복해~~~').encode('utf_8'))
        
        
except socket.error as err:
    print('err : ', err)
    sys.exit()
    
finally:
    conn.close()
    serverSock.close()
    
