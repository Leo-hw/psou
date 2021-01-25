from django.urls import path
from myboard import views


urlpatterns = [
    path('', views.DispFunc, name="disp"),          #/gogo/
    path('<int:question_id>', views.DetailFunc, name = 'detail'),
    #path('<타입:이름>', function, 이름)
    path('<int:question_id>/vote/', views.VoteFunc, name = 'vote'),           #    /gogo/1/vote
    path('<int:question_id>/results/', views.ResultFunc, name = 'results'),           #    /gogo/1/results
]