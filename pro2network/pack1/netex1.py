'''
# 네트워크 : 네트워크에 필요한 구성 요소들(케이블, 라우터, 무선링크, 장비...)
# 네트워킹 : 네트워크 데이터를 컴퓨터 간에 주고 받는 과정 / 송, 수신.
# socket  : 네트워크를 위한 통신 채널 - TCP/IP 기반의 프로그래밍 인터페이스
                     응용 계층과 전송 계층 사이에 존재하는 전송용 API

# 네트워크 연결 방식
1. tcp : 연결이 지속되는 방식. 실시간 통신 가능. 신뢰도가 높으나 네트워크에 부하가 걸리기 쉽다.
         Socket, ServerSockt을 주로 사용.
2. www 기반의 URL은 Uniform Resource Locator의 약어가 URL이다. 자바의 URL클래스는 URL통신을 가능하게 한다.
3. udp : 비연결성 통신방식. 신뢰도는 낮으나 네트워크에 부하가 덜하다.
         DataGramSocket, DataGramPacket, MultiCastScoket을 주로 사용
'''
import socket

print(socket.getservbyname('http', 'tcp'))        #80    www 환경에서 사용
print(socket.getservbyname('telnet', 'tcp'))    #23    원격 컴 접속시 사용
print(socket.getservbyname('ftp', 'tcp'))          #21    파일 전송시 사용
print(socket.getservbyname('pop3', 'tcp'))      #110  이메일 수신 시
print(socket.getservbyname('smtp', 'tcp'))      #25    이메일 송, 수신

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP)) # [(<AddressFamily.AF_INET: 2>, 0, 6, '', ('210.89.164.90', 80)), (<AddressFamily.AF_INET: 2>, 0, 6, '', ('125.209.222.141', 80))]
