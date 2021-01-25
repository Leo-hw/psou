# client 로 server 에 접속 - socket

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) 
clientSock.connect(('192.168.0.72',7788))  # 능동적으로 server 에 접속을 시작.

# packet(header+body) 단위로 전송 - sequential 한 binary data 형태로 전송.
clientSock.sendall('행복해'.encode(encoding='utf_8', errors='strict'))

recieve_msg = clientSock.recv(1024).decode()
print('수신 자료 : ' + recieve_msg)

clientSock.close()


