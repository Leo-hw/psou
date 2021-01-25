from django.contrib import admin
from sangpumapp.models import Maker, Product

# Register your models here.
class MakerAdmin(admin.ModelAdmin):         # pep8 guide line 에 띄워쓰라고 나옴... 내가 보진 않음.
    list_display = ('id', 'mname', 'tel', 'addr')
    
admin.site.register(Maker, MakerAdmin)


class ProductAdmin(admin.ModelAdmin):         # pep8 guide line 에 띄워쓰라고 나옴... 내가 보진 않음.
    list_display = ('id', 'pname', 'price', 'maker_name')
    
admin.site.register(Product , ProductAdmin)
    
    