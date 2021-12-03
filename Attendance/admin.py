from django.contrib import admin
from .models import Student,MasterData

#admin.site.register(Student)
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['stuname', 'stumail', 'stuclass']

@admin.register(MasterData)
class MasterDataadmin(admin.ModelAdmin):
	list_display = ['stuid', 'stuname', 'stumail', 'subject']
