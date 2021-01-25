from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect
from datetime import datetime

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    #gdata = Guest.objects.all()
#     print(gdata)                                        # <QuerySet [<Guest: 너무춥다>]>    // queryset 반환
#     print(Guest.objects.get(id=1))      # 너무춥다                                                    // object 반환
#     print(Guest.objects.filter(id=1))   #<QuerySet [<Guest: 너무춥다>]>    // queryset 반환
#     print(Guest.objects.filter(title__contains ='안녕'))      # <QuerySet []> // 내용에 있으면 반환하고, queryset 이 없으면 빈칸
    
    #정렬방법1
    #gdata = Guest.objects.all().order_by('title')           # title 별 ascending sort
    #gdata = Guest.objects.all().order_by('-title')           # title 별 descending sort
    #gdata = Guest.objects.all().order_by('-id')[0:3]        #slicing 처리
    gdata = Guest.objects.all()          
    context = {'gdata': gdata}
    return render(request, 'list.html', context)


def InsertFunc(request):
    return render(request, 'insert.html')
    
def InsertFuncOk(request):
    if request.method == 'POST':
        
        #print(request.POST.get('title'))
        #print(request.POST['title'])            #  위와 결과는 동일하다.
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()
            ).save()                # 레코드 추가.  insert into myguest_guest values(...) 
            
        '''
            #수정
            g = Guest.objects.get(id = 1)
            g.title = request.POST.get('title')
            g.save()            # update myguest_guest set title...
        
           #삭제
            g = Guest.objects.get(id = 1)
            g.delete()        # delete from myguest_guest where id = 1
        '''
            
        return HttpResponseRedirect('/guest')       # 추가 후 목록보기.
        