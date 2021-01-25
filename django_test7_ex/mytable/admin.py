from django.contrib import admin
from mytable.models import Jikwon, Buser, Gogek

# Register your models here.
class JikwonAdmin(admin.ModelAdmin):
    list_display = ('jikwon_no', 'jikwon_name', 'buser_num', 'jikwon_jik', 'jikwon_pay', 'jikwon_ibsail', 'jikwon_gen', 'jikwon_rating')
admin.site.register(Jikwon, JikwonAdmin)

class BuserAdmin(admin.ModelAdmin):
    list_display = ('buser_no', 'buser_name', 'buser_loc', 'buser_tel')
admin.site.register(Buser, BuserAdmin)

class GogekAdmin(admin.ModelAdmin):
    list_display = ('gogek_no', 'gogek_name', 'gogek_tel', 'gogek_jumin', 'gogek_damsano')
admin.site.register(Gogek, GogekAdmin)