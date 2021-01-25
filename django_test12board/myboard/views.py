from django.shortcuts import render, get_object_or_404
from myboard.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse            #url 패턴으로부터 url 스트링 얻기

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list} 
    return render(request, 'display.html', context)


def DetailFunc(request, question_id):       # gogo/1          <===     question_id (1이 question_id 값.)
    #return HttpResponse('question_id%s'%question_id)      # 결과 : question_id 1 또는 2
    '''        아래와 같은 의미.
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    '''
    question = get_object_or_404(Question, pk = question_id)            # 위 주석과 같은 의미
#     print(question.question_text)
#     print(question)
#     print(question.pub_date)
    
    return render(request, 'detail.html', {'question':question})

def VoteFunc(request, question_id):
    #return HttpResponse("voting on question_id%s"%question_id)
    question = get_object_or_404(Question, pk = question_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_msg':'1개의 항목을 반드시 선택하시오'})
    #print(sel_choice)
    
    
    sel_choice.votes +=1            # 선택된 항목에 득표 누적.
    sel_choice.save()           # (득표 변경 사항)수정 완료 //Choice 테이블에 votes 수정 완료 
    #print(reverse('results', args = (question.id,)))            
    
    #return render(request, 'results.html')
    return HttpResponseRedirect(reverse('results', args = (question.id,)))


def ResultFunc(request, question_id):
    print('result of question_id:%s'%question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'results.html', {'question':question})
        
    

  
  
  
    