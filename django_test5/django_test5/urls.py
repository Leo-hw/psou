"""django_test5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import MyClass1,MyClass2,MyClass3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexFunc),
    path('calldict/', views.CalldictFunc),
    
    #path('disp1/', MyClass1.as_view()),
    # 아래 방식으로는 별도의 클래스를 작성할 필요가 없이 해당 html 파일을 출력.
    path('disp1/', MyClass1.as_view(template_name='disp1.html')),
    
    path('disp2/', MyClass2.as_view()),
    path('disp3/', MyClass3.as_view()),
]
