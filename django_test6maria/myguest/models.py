from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno = models.AutoField(auto_created = True, primary_key = True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    def __str__(self):
        return self.title               # 요거를 써서, objects.all() 사용했을 때, 제목을 볼 수 있다~//<QuerySet [<Guest: 너무춥다>]>
    
    #정렬방법 2
    class Meta:
        #ordering = ('title',)        # title 오름차순    : tuple type 이어야 한다.
        #ordering = ('title','id')       #n차 키 부여 가능
        #ordering = ('-title',)
        ordering = ('-id',)  
        
        