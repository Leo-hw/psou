from django.db import models

# Create your models here.
class Buser(models.Model):
    buser_no = models.IntegerField(primary_key=True)
    buser_name = models.CharField(max_length=10)
    buser_loc = models.CharField(max_length=10, blank=True, null=True)
    buser_tel = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buser'
        
class Gogek(models.Model):
    gogek_no = models.IntegerField(primary_key=True)
    gogek_name = models.CharField(max_length=10)
    gogek_tel = models.CharField(max_length=20, blank=True, null=True)
    gogek_jumin = models.CharField(max_length=14, blank=True, null=True)
    gogek_damsano = models.ForeignKey('Jikwon', models.DO_NOTHING, db_column='gogek_damsano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gogek'

class Jikwon(models.Model):
    jikwon_no = models.IntegerField(primary_key=True)
    jikwon_name = models.CharField(max_length=10)
    buser_num = models.IntegerField()
    jikwon_jik = models.CharField(max_length=10, blank=True, null=True)
    jikwon_pay = models.IntegerField(blank=True, null=True)
    jikwon_ibsail = models.DateField(blank=True, null=True)
    jikwon_gen = models.CharField(max_length=4, blank=True, null=True)
    jikwon_rating = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jikwon'
