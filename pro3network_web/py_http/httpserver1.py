'''
Simple HTTPServer 구축 후 http 서비스 진행
        - GET, HEAD 처리 가능
        - POST, CGI 처리 불가
'''

# HTTPServer : 기본적인 Socket 연결을 관리.
# SimpleHTTPRequestHandler : 클라이언트의 요청 처리 (GET, HEAD)

from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 7777

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', port), handler)
print('웹 서비스 시작~!!~~!@~!@~!@!~@~!@~!@~!@~!@~!@')

serv.serve_forever()
