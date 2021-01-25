from django.shortcuts import render
def Main(request):
    ss = "<div><b style='font-size:40px;'>메인화면</b></div>"
    return render(request, 'main.html', {'head':ss})