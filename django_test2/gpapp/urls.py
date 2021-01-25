'''
메인 urls에 의해 위임된 각 application의 urls
'''
from django.urls import path
from gpapp import views

urlpatterns = [
    path('', views.InsertFunc, name='InsertFunc'),                  
]

