from django.contrib import admin
from freeBoard.models import Fboard

@admin.register(Fboard)
class FboardAdmin(admin.ModelAdmin):
    list_display = ['b_no','b_title','b_date']
