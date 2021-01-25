from django.shortcuts import render
from myapp.models import Profile
from django.db.models.aggregates import Avg, Count, Max, Min, Sum
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# Create your views here.
def IndexFunc(request):
    return render(request, 'index.html')

def CalldictFunc(request):
    profile_list = Profile.objects.all()
    #print(profile_list)
    
    for row in profile_list.values_list():
        print(row)      # (1, '홍길동', 123)...
    
    print(Profile.objects.aggregate(Avg('age')))
    print(Profile.objects.aggregate(Max('age')))
    print(Profile.objects.aggregate(Sum('age')))
    print(Profile.objects.aggregate(Count('age')))
    print(len(profile_list))
    
    print(Profile.objects.filter(name='홍길동').aggregate(Avg('age'))) #filter =  where 조건문과 동일
    
    # values() + aggregates()            그룹별 평균 나이는?
    qs = Profile.objects.values('name').annotate(Avg('age'))
    for r in qs:
        print(r)
    
### 결과(그룹별 평균)###
# {'name': '너는왜', 'age__avg': 123.0}
# {'name': '신기해', 'age__avg': 222.5}
# {'name': '한가해', 'age__avg': 11.0}
# {'name': '홍길동', 'age__avg': 59.333333333333336}
    
    #결과를 list 로 감싸 dict type으로 클라이언트에게 출력하기
    
    pro_list =[]
    for pro in profile_list:
        pro_dict ={}
        pro_dict['name'] = pro.name
        pro_dict['age'] = pro.age
        pro_list.append(pro_dict)
        print(pro_list)
    context = {'pro_dicts':pro_list}
    return render(request, 'abc.html', context)

# GenericView 관련
class MyClass1(TemplateView):
    template_name = 'disp1.html'
    def get(self, request):
        return render(request, self.template_name)

class MyClass2(TemplateView):
    def get(self, request):
        return render(request, 'hi.html')
    
    def post(self, request):
        msg = request.POST.get('msg')
        return render(request, 'hi2.html', {'msg' : msg + ' 만세'})
    
class MyClass3(ListView):
    model = Profile             # 해당 테이블의 자료를 읽어 object_list 키에 담은 후, profile_list.html 파일을 호출 # 현재 app 이름/profile_list.html 파일을 호출
    
    
    
