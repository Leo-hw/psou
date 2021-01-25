from django.shortcuts import render
from company.models import Gogek
from datetime import datetime
from django.utils import timezone

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def InfoFunc(request):
    if request.method == "GET":
        return render(request, 'infosearch.html')
    elif request.method == "POST":
         = Gogek.objects.get(
            gogek_name = request.POST.get('gogek_name'),
            gogek_tel = request.POST.get('gogek_tel'))

        gogekinfo.gogek_damsano.jikwon_ibsail = \
            datetime.now().year - gogekinfo.gogek_damsano.jikwon_ibsail.year
        # 참고
        # 한국 시간(UTC+9)을 사용하기 위해 django 프로젝트의 settings.py 에 아래와 같이 설정을 합니다.
        # USE_TZ = True
        # TIME_ZONE = 'Asia/Seoul' 한 후에
        # now = timezone.localtime().year
        # print('now : ', now)
        
        if gogekinfo.gogek_damsano.jikwon_rating == 'a':
            gogekinfo.gogek_damsano.jikwon_rating = '최우수'
        elif gogekinfo.gogek_damsano.jikwon_rating == 'b':
            gogekinfo.gogek_damsano.jikwon_rating = '우수'
        elif gogekinfo.gogek_damsano.jikwon_rating == 'c':
            gogekinfo.gogek_damsano.jikwon_rating = '일반'
  
        return render(request, 'infosearch.html', {'info':gogekinfo})