from django.shortcuts import render
from mysangpum.models import Sangdata
import MySQLdb
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


######### SQL 문 직접 사용하기 위해 ##########
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
###############################

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
#     # SQL 문 사용
#     sql = "select * from sangdata"
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     
#     datas = cursor.fetchall()               # 튜플
#     print(type(datas))
     
    # django ORM method 장고의 ORM 지원 메소드
    ##########################################      페이징 없는 경우
    '''
    datas = Sangdata.objects.all()             # 쿼리 세트
    #print(datas)
    return render(request, 'list.html', {'sangpums':datas})
    ### datas 와 datas2 의 return type 이 다름.
    '''
    
    ##########################################       페이징 있는 경우
    datas = Sangdata.objects.all().order_by('-code')
    paginator  = Paginator(datas, 5)        # 한 페이지 당 3개씩 출력.
    
    try :
        page = request.GET.get('page')
        
    except :
        page = 1
    
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:    # page 가 정수가 아닐 때
        data = paginator.page(1)
        
    except EmptyPage :      # page 가 받아지지 않은 경우
        data = paginator.page(paginator.num_pages())
        
    # 개별 페이지 표시용
    allpage = range(paginator.num_pages + 1)
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        #code = request.POST.get("code")
        # 여기서는 자료 검증 생략함. 원래는 필요한 부분.
        # insert into sangdata... 사용 가능 -- 그러나..

        # 새로 등록한 코드 번호 검증 작업 필요... insert 전에 select 로 코드가 있는 지 확인 후, 입력하도록.
        
        Sangdata(
            code = request.POST.get("code"),
            sang = request.POST.get("sang"),
            su = request.POST.get("su"),
            dan = request.POST.get("dan") 
            ).save()
        print(Sangdata())
        return HttpResponseRedirect('/sangpum/list')        # 추가 후 상품 보기
        
        
        
        
        
def UpdateFunc(request):
    data = Sangdata.objects.get(code = request.GET.get('code'))
    return render(request, 'update.html',{'sang_one':data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        #update sangdata set sang = ... 이런식으로 sql 문 사용도 가능
        updateRec = Sangdata.objects.get(code=request.POST.get('code'))
        
        updateRec.sang = request.POST.get('sang')
        updateRec.su = request.POST.get('su')
        updateRec.dan = request.POST.get('dan')
        updateRec.save()
        
    return HttpResponseRedirect('/sangpum/list')            # 수정 후 상폼 보기

def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list')            # 삭제 후 상폼 보기

