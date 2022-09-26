from django.urls import path,include
from . import views

app_name = "member"
urlpatterns = [
    # 회원전체리스트
    path('memList/',views.memList,name="memList"),
    # 회원상세페이지
    path('<str:m_id>/memView/',views.memView,name="memView"),
    # 회원수정페이지
    path('<str:m_id>/memUpdate/',views.memUpdate,name="memUpdate"),
    # 회원수정저장
    path('memUpdateOk/',views.memUpdateOk,name="memUpdateOk"),
    # 회원정보삭제
    path('<str:m_id>/memDelete/',views.memDelete,name="memDelete"),
    
    # 회원가입 호출
    path('memWrite/',views.memWrite,name="memWrite"),
    # 회원정보 저장
    path('memWriteOk/',views.memWriteOk,name='memWriteOk'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그인체크
    path('loginOk/', views.loginOk, name="loginOk"),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
]
