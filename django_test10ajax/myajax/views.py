from django.shortcuts import render
import json
from conda.common.serialize import json_dump
from django.http.response import HttpResponse


# dict data
lan = {
    'id': 111,
    'name': '홍길동',
    'history':[
            {'date':'2010-7-20', 'exam':'basic'},
            {'date':'2010-7-20', 'exam':'django'},
        ]
    
    }
# Create your views here.
def IndexFunc(request):
#     print(type(lan))        # class:dict
    
    
    # json encoding :dict(list, tuple...) => string(문자열로 변환하는 작업 
    jsonString = json_dump(lan)
#     print(jsonString)
#     print(type(jsonString))
    
    #들여쓰기가 있는 형태로 변환
    jsonString = json.dumps(lan, indent =4)
    print(jsonString)
    
    
    print('%%%%'*20)
    # json Decoding : str(문자열 -key : value 형태 ) => dict 로 변환하는 작업.
    dictData = json.loads(jsonString)
#     print(dictData)
#     print(type(dictData))
#     print(dictData['name'])         # python 의 dict 클래스 관련 명령어를 사용할 수 있다.
    for h in dictData['history']:
        print(h['date'], h['exam'])
        
    return render(request, 'abc.html')


def Func1(request):
    msg = request.GET['msg']
    #print(msg)
    msg = msg+'kt wiz'
    context = {'key':msg}
    return HttpResponse(json.dumps(context), content_type="application/json")

def Func2(request):
    datas = [
        {'irum':'홍길동', 'nai': 22},
        {'irum':'고길동', 'nai': 32},
        {'irum':'신길동', 'nai': 52},
        ]
    return HttpResponse(json.dumps(datas), content_type="application/json")

