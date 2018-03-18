from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(Facility)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','type','id')
admin.site.register(Users,UserAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text','fid','index','id','date')
admin.site.register(Comments,CommentsAdmin)