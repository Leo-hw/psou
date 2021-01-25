from http.server import CGIHTTPRequestHandler, HTTPServer

port = 9999
           
class HandlerClass(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin'] #(/'cgi-bin')도 가능
    
    
serv = HTTPServer(('127.0.0.1', port), HandlerClass)
print('-----------------------웹 서비스 시작------------------------')

serv.serve_forever()
 