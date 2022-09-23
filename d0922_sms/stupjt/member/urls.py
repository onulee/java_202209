from django.urls import path,include
from . import views

app_name = "member"
urlpatterns = [
    # 회원가입 호출
    path('memWrite/',views.memWrite,name="memWrite"),
    # 회원정보 저장
    path('memWriteOk/',views.memWriteOk,name='memWriteOk'),
    # 로그인
    path('login/', views.login, name='login'),
]
