from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def setosFunc(request):
    if 'favorite_os' in request.GET:
        #print(request.GET['favorite_os'])
        request.session['f_os'] = request.GET['favorite_os']            # request.session['key'] = value 세션 읽기 /쓰기
        #kbs = request.session['f_os'] = request.GET['favorite_os']
        #print(request.GET['favorite_os'])
        return HttpResponseRedirect('/showos')      # showos 요청 발생.            
    else :
        return render(request, 'setos.html')            # forwarding
    
def showosFunc(request):
    context = {}            # dict type 
    #print(request.session['f_os'])
    if 'f_os' in request.session:   # 세션 key 중에 f_os 가 있다면,
        context['dict_f_os'] = request.session['f_os']
        context['f_os'] = request.session['f_os']       # 세션 값 읽기.
        context['message'] = '당신이 선택한 운영체제는 %s'%request.session['f_os']
        
    else:
        context['f_os'] = None
       
        context['message'] = '운영체제를 선택하지 않으셨네요.'
    
    request.session.set_expiry(5)           #5초 동안 클라이언트의 활동이 없으면 세션 삭제.
    return render(request, 'show.html', context)
        
        
        