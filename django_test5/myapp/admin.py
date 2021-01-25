from django.contrib import admin
from myapp.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    
admin.site.register(Profile, ProfileAdmin)