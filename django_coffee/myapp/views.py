from django.shortcuts import render
import MySQLdb
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from myapp.models import Survey
from django.http.response import  HttpResponseRedirect
import scipy.stats as stats

plt.rc('font', family='malgun gothic')                        # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False           # 음수 부호 깨짐 방지
plt.style.use('ggplot')

# Create your views here.

def MainFunc(request):
    return render(request, 'main.html')


def SurveyFunc(request):
    return render(request, 'survey.html')
    
def SurveyOk(request):
   
    if request.method == 'POST':
        Survey(
                gender = request.POST.get('gender'),
            #     print(gen)
                age = request.POST.get('age'),
                co_survey = request.POST.get('co_survey')
            ).save()        ## 저장
        return HttpResponseRedirect('list')
        
def List(request):        
    survey = Survey.objects.all()
    datas = []
    for s in survey:
        dic = {'gender': s.gender, 'age':s.age, 'co_survey':s.co_survey}
        datas.append(dic)
    
    df = pd.DataFrame(datas)
    data2 = pd.crosstab(index = df['gender'], columns=df['co_survey'], margins=True)
    
    chi, p, _, _ = stats.chi2_contingency(data2)
    print('chi : ' , chi, ' p-value : ' ,p)
    print(data2)
    dff = df.to_html()
    
    x = np.arange(len(data2.columns))
    plt.bar(x - 0.15,data2.loc['남'], width=0.3)
    plt.bar(x + 0.15,data2.loc['여'], width=0.3)
    plt.xticks(x, data2.columns)
    plt.legend(data2.index)
    fig = plt.gcf()     ## 저장 준비
    fig.savefig('C:/work/psou/django_coffee/myapp/static/images/test_matplot1.png')
    
    return render(request, 'list.html', {'dff':dff, 'p':p})

        
    
    