from django.contrib import admin
from myfiles.models import Student
# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','ism','tg_id','fam','username']
admin.site.register(Student,AdminStudent)