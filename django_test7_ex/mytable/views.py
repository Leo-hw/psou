from django.shortcuts import render
from mytable.models import Jikwon, Buser, Gogek
from django.db.models import Count
from django.db.models.functions.text import Substr

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def JikwonFunc(request):
    jikwons = Jikwon.objects.all()
    jcount = len(jikwons)
    #print(jikwons)
    #print(jcount)
    return render(request, 'jiklist.html', {'jikwons': jikwons})

def BuserFunc(request):
    busers = Buser.objects.all()
    bcount = len(busers)
    #print(busers)
    #print(bcount)
    return render(request, 'bulist.html', {'busers':busers, 'bcount':bcount})

def GogekFunc(request):
    gogeks = Gogek.objects.all()
    gcount = len(gogeks)
    return render(request, 'golist.html', {'golist':gogeks})

def JikwonSearch(request):
    buser_sno = request.GET.get('buser_num')
    #jikwons  = Jikwon.objects.select_related('gogek').get('gogek_no')
    jikwons  = Jikwon.objects.all().filter(buser_num=buser_sno)
    #jikwon_sno = Jikwon.objects.aggregate('jikwon_no')
    
#         강사님이 하신 방법.
#     no = int(request.GET.get('no'))
#     empData = Jikwon.objects.filter(buser_num = no).order_by('-jikwon_no')
# 
#     customerData = Gogek.objects.values('gogek_damsano').annotate(count = Count('gogek_no')).values('gogek_damsano', 'count')
# 
#     datas = []
#         for eData in empData:
#             cnt = 0
#             for cData in customerData:
#                 if eData.jikwon_no == cData["gogek_damsano"]:
#                     cnt = cData["count"]
# 
#             newEmpData = {}
#             newEmpData["jikwon_no"] = eData.jikwon_no
#             newEmpData["jikwon_name"] = eData.jikwon_name
#             newEmpData["jikwon_jik"] = eData.jikwon_jik
#             newEmpData["count"] = cnt
#             datas.append(newEmpData)
#     
#         print(datas)
    
    
    for i in jikwons:
        gogeksu = Gogek.objects.all().filter(gogek_damsano=i.jikwon_no).count()
        #print(gogeksu)
        i.gogeksu = gogeksu
    # 관리고객 구하기.
    return render(request, 'jiklist.html', {'jikwons': jikwons})

def GogekSearch(request):
    gogek_sano = request.GET.get('gogek_damsano') 
    gogeks = Gogek.objects.all().filter(gogek_damsano=gogek_sano)
    
    for g in gogeks:
        if g.gogek_jumin[7:8] == '1':
            g.gogek_gen = '남'
        elif g.gogek_jumin[7:8] == '2':
            g.gogek_gen = '여'
            
    gcount = len(gogeks)
    return render(request, 'golist.html', {'gogeks' : gogeks, 'gcount':gcount})

