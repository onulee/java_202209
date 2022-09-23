from django.contrib import admin
from students.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_no','s_name','s_date']