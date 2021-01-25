from django.db import models

# Create your models here.


class Table(models.Model):
    m_id = models.CharField(max_length=10)
    irum = models.CharField(max_length=20)
    juso = models.CharField(max_length=100)
    nai = models.IntegerField()