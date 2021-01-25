from myapp import views
from django.urls.conf import path


urlpatterns = [
    path('', views.GogekFunc),
    path('search/', views.GogekSearch),
    ]