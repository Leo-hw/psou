from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect
from datetime import datetime

def ListFunc(request):                  # 페이징 처리.
    #datas = BoardTab.objects.all().order_by('-id')
    datas = BoardTab.objects.all().order_by('-gnum', 'onum')            # 댓글이 달릴 경우 
    paginator = Paginator(datas, 5)
    page = request.GET.get('page')
    
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
    
    return render(request, 'board.html', {'data':data})


def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        #print('1')
        try:
            gbun = 1
            datas = BoardTab.objects.all()          # group 번호 구하기
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id +1
            BoardTab(
                name = request.POST.get('name'),
                passwd= request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = Get_ip_address(request),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0,
                ).save()
        except Exception as e :
            print('추가 오류 :' + str(e))
        
    #return HttpResponseRedirect('/board/list/')          # 추가 후 목록보기.    
    return redirect('/board/list/') 

def Get_ip_address(request):           # 클라이언트 ip 얻기
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        ip = x_forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ContentFunc(request):       # 글 내용 상세 보기
    data = BoardTab.objects.get(id=request.GET.get('id'))
    data.readcnt = data.readcnt +1
    data.save()     # 수정
    page = request.GET.get('page')
    return render(request, 'content.html', {'data_one':data, 'page': page})
                

def UpdateFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print('UpdateFunc err:' + str(e))
    return render(request, 'update.html', {'data_one': data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = BoardTab.objects.get(id=request.POST.get('id'))
        # 비밀번호 비교
        if upRec.passwd == request.POST.get('up_passwd'):
            upRec.name = request.POST.get('name')
            upRec.mail = request.POST.get('mail')
            upRec.title = request.POST.get('title')
            upRec.cont = request.POST.get('cont')
            upRec.save()
            
        else:
            return render(request, 'error.html')
        
    return HttpResponseRedirect('/board/list/')         # 수정 후 목록보기.

def DeleteFunc(request):        # 삭제용
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print('DeleteFunc err:' + str(e))
    return render(request, 'delete.html', {'data_one': data})


def DeleteOkFunc(request):
    if request.method == 'POST':
        delRec = BoardTab.objects.get(id=request.POST.get('id'))
        # 비밀번호 비교
        if delRec.passwd == request.POST.get('del_passwd'):
            delRec.delete()         # delete from boardtab where id = 아이디
        else:
            return render(request, 'error.html')
        
    return HttpResponseRedirect('/board/list/')         # 삭제 후 목록보기.

def SearchFunc(request):               # 검색 기능: 작성자 / 제목 별
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        #print('s_type:', s_type, 's_value:',s_value)
        
        if s_type == 'title':
            datas = BoardTab.objects.filter(title__contains = s_value).order_by('-id')
        elif s_type == 'name':
            datas = BoardTab.objects.filter(name__contains = s_value).order_by('-id')
        
        paginator = Paginator(datas, 5)
        page = request.GET.get('page')    

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages())
    
    return render(request, 'board.html', {'data':data})

def ReplyFunc(request):     # 댓글용
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))           # 댓글 ㅐ대상자료 읽기
    except Exception as e:
        print('replyFunc err' + str(e))
        
    return render(request, 'reply.html', {'data_one': data})

def ReplyOkFunc(request):
    if request.method == 'POST':
        try:
            regnum = int(request.POST.get('gnum'))
            reonum = int(request.POST.get('onum'))
            temRec = BoardTab.objects.get(id=request.POST.get('id'))
            
            old_gnum = temRec.gnum
            old_onum = temRec.onum
            if old_onum >= reonum and old_gnum == regnum:
                old_onum = old_onum+1                   # onum 갱신
                
            # 댓글 저장.
            BoardTab(
                name = request.POST.get('name'),
                passwd= request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = Get_ip_address(request),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = regnum,
                onum = old_onum,
                nested = int(request.POST.get('nested'))+1,
                ).save()
                
            print(BoardTab.gnum, BoardTab.onum)
        except Exception as e:
            print('replyOkFunc err' + str(e))

    return redirect('/board/list/')         # 댓글 입력 후 목록보기.