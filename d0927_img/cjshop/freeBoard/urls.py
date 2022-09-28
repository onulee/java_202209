from django.urls import path,include
from . import views

app_name="freeBoard"
urlpatterns = [
    path('fboardList',views.fboardList,name="fboardList"),
    path('fboardWrite',views.fboardWrite,name="fboardWrite"),
]
