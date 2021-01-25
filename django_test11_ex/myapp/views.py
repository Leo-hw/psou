from django.shortcuts import render
from myapp.models import Jikwon, Buser
from django.http.response import HttpResponse
import json

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    return render(request, 'list.html')



def ListDbFunc(request):
    #sdata = Jikwon.objects.all().filter(request.POST.get('jik'))
    sdata = Jikwon.objects.select_related('buser').filter('jikwon_jik')
    bdata = Buser.objects.all()
    datas=[]
    
    for s in sdata:
        dic = {'jikwon_no':s.jikwon_no,'jikwon_name':s.jikwon_name}
        datas.append(dic)
    for b in bdata:
        bdic = {'buser_name':b.buser_name}
        datas.append(bdic)
    print(datas)
    
    return HttpResponse(json.dumps(datas), content_type="application/json")