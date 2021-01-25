'''
HTTPServer 구축 후 http 서비스 진행
# CGIHTTPRequestHandler : client 와 server 사이에 통신이 가능// 동적 처리 가능. 
        - GET, HEAD ,POST, CGI 처리 가능
        - CGI  : 웹 서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약, 대화형 웹 페이지를 구현
                    : 클라이언트가 요청한 db 자료 처리후 출력
                    : form 을 사용한 자료 전송, 메일 전송
'''

from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8888
           
class HandlerClass(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin'] #(/'cgi-bin')도 가능
    
    
serv = HTTPServer(('127.0.0.1', port), HandlerClass)
print('웹 서비스 시작~!!~~!@~!@~!@!~@~!@~!@~!@~!@~!@')

serv.serve_forever()
 