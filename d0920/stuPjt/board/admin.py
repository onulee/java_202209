from django.contrib import admin
from board.models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['b_no','b_title','b_date']
