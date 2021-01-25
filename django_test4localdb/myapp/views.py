from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')


def DbShow(request):
    #ORM 을 통한 Query
    datas = Article.objects.all()       # select * from article 과 동일.        # 내부적으로 select 문이 수행
    #print(datas)                    
    #print(datas[0].name)
    
    
    #return render(request, 'articlelist.html')
    return render(request, 'articlelist.html', {'articles' : datas})         # QuerySet 을 전달.