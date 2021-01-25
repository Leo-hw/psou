from django.db import models

# Create your models here.
# 투표 질문
class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default = 0)
    
