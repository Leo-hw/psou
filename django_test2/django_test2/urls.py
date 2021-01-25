"""django_test2 URL Configuration

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
from gpapp import views
from gpapp.views import MyCallView
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),                                            # !!!요청명과 application 명은 달라야 함.
    path('', views.MainFunc, name='MainFunc'),                  # 1. function views 방법.(제일 많이 사용되는 방법)
    path('gpapp/callget/', MyCallView.as_view()),             # 2.class -based views
    path('gpapp/insert/', include('gpapp.urls')),                  # 3. Including another URL conf(위임하는 방법)- 권한 넘겨주기. gpapp 안에 있는 urls 에게 권한 위임.
]
