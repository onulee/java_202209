from django.contrib import admin
# models연결
from students.models import Student

# Student객체만 출력
# admin.site.register(Student)

# s_name,s_major2개 컬럼 출력
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name','s_major']