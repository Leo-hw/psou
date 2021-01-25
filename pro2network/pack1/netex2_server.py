# 단발성 Echo Server
from socket import *

#socket (tcp/ip)
serverSock = socket(AF_INET, SOCK_STREAM)   # 종류, 유형
serverSock.bind(('192.168.0.72', 9999))
serverSock.listen()         # 클라이언트와 연결 수 1~5  까지 줄 수 있음.// 한번에 받아들일 수 있는게 5개.

print('에코서버 서비스 중...')

conn, addr = serverSock.accept()        # 연결 대기 - 수동적으로 대기
print('client addr : ', addr)
print('client addr :  ', conn)

print('클라이언트로부터 넘어온 정보 수신 결과 :', conn.recv(1024).decode())
conn.close()
serverSock.close()
