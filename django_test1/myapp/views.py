from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('요청 처리')

def helloFunc(request):
    msg = 'Hola Todos!'
    ss = "<html><body>Nice%s</body></html>"%(msg)
    return HttpResponse(ss)
    
def hello_temp_Func(request):
    msg = '홍길동'
    return render(request, 'show.html', {'name':msg})

def worldFunc(request):
    return render(request, 'disp.html')