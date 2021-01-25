from django.contrib import admin
from myfriend.models import Table

# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display = ('m_id', 'irum', 'juso', 'nai')
    
admin.site.register(Table, TableAdmin)