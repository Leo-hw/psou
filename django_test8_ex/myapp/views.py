from django.shortcuts import render
import MySQLdb
from myapp.models import Jikwon, Gogek



config = {                       
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

conn = MySQLdb.connect(**config)

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def GogekFunc(request):
    return render(request, 'gogek.html')

def GogekSearch(request):
    gogek_name = request.POST.get('name')
    print(gogek_name)
    jikdata = Jikwon.objects.all().select_related
    ('gogek_name')
    print(jikdata)
    datas = []
    for j in jikdata:
        print(j.jikwon_name)
        dicData = {'jikwon_name': j.jikwon_name,
                   'jikwon_jik': j.jikwon_jik,
                   'buser_name':j.buser_name,
                   'buser_tel':j.buser_tel
                   }
        datas.append(dicData)
        print(datas)
     
    return render(request, 'gogeksearch.html', {'datas': datas})