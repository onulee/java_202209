from django.contrib import admin
from students.models import Student

# 1개의 정보출력
# admin.site.register(Student)

# 여러개 정보출력
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name','s_major','s_age']
    
admin.site.register(Student,StudentAdmin)    