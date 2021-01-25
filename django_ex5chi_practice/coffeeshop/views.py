from django.shortcuts import render
from coffeeshop.models import Survey
from django.http.response import HttpResponseRedirect
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SurveyFunc(request):
    return render(request, 'survey.html')

def InsertFunc(request):
    if request.method == 'POST':
        Survey(
                gender = request.POST.get('gender'),
            #     print(gen)
                age = request.POST.get('age'),
                co_survey = request.POST.get('co_survey')
            ).save()        ## 저장
        return HttpResponseRedirect('list')
def ListFunc(request):
    surveydata = Survey.objects.all()
    gen = []
    nai = []
    co = []
    for s in surveydata:
        gen.append(s.gender)
        nai.append(s.age)
        co.append(s.co_survey)
    dict = {
        'gender':gen,
        'age':nai,
        'co_survey':co,
        }
    data = pd.DataFrame(dict)
#     print(data)
    ctab = pd.crosstab(index = data['gender'], columns=data['co_survey'])
#     print(ctab.columns)
    _, p, _, _ = stats.chi2_contingency(ctab)
    pvalue = p
    ct = ctab.to_html()
    x = np.arange(len(ctab.columns))
    
    plt.bar(x - 0.15,ctab.loc['남'], width=0.3)
    plt.bar(x + 0.15,ctab.loc['여'], width=0.3)
    plt.xticks(x, ctab.columns)
    plt.legend(ctab.index)
    fig = plt.gcf()     ## 저장 준비
    fig.savefig('C:/work/psou/django_ex5chi_practice/coffeeshop/static/image/test_matplot1.png')
    
    return render(request, 'list.html',{'ctab':ct, 'p':pvalue})