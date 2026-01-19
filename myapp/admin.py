from django.contrib import admin

# Register your models here.
from myapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','email','images']
admin.site.register(Student,StudentAdmin)    
