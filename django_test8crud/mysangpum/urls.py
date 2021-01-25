
from mysangpum import views
from django.urls.conf import path

urlpatterns = [
    path('list/', views.ListFunc),
    path('insert', views.InsertFunc),
    path('insertok', views.InsertOkFunc),
    path('update', views.UpdateFunc),
    path('updateok', views.UpdateOkFunc),
    path('delete/', views.DeleteFunc),
    
    ]