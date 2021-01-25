from django.shortcuts import render
from myfriend.models import Table

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ShowFunc(request):
    datas = Table.objects.all()
    print(datas)
    return render(request, 'show.html', {'table':datas})