# client 로 server 에 접속 - socket

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) 
clientSock.connect(('192.168.0.72',9999))  # 능동적으로 server 에 접속을 시작.

# packet(header+body) 단위로 전송 - sequential 한 binary data 형태로 전송.
clientSock.sendall('안녕 반가워  leo'.encode(encoding='utf_8', errors='strict'))
clientSock.close()


