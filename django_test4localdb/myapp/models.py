from django.db import models

# Create your models here.
# ORM 기법을 사용 : SQL 문 직접 기술 X
# table 을 클래스로 정의
#컬럼은 속성(멤버 변수)로 부여 (전역변수)             
# varchar, char
 
 
class Article(models.Model):            
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    

