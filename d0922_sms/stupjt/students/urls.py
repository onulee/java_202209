from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    # 학생등록페이지 호출
    path('stuWrite/',views.stuWrite,name='stuWrite'),
    # 학생등록데이터 저장
    path('stuWriteOk/',views.stuWriteOk, name="stuWriteOk"),
    # 학생전체리스트
    path('stuList/',views.stuList, name="stuList"),
    # 학생상세페이지 호출
    path('<str:s_no>/stuView/',views.stuView,name="stuView"),
    # 학생수정페이지 호출
    path('<str:s_no>/stuUpdate/',views.stuUpdate,name='stuUpdate'),
    # 학생수정데이터 저장
    path('stuUpdateOk/',views.stuUpdateOk,name='stuUpdateOk'),
    # 학생정보 삭제
    path('<str:s_no>/stuDelete/',views.stuDelete,name="stuDelete"),
]
