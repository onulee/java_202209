from . import views
from django.urls import path,include

# 별칭
app_name=''
urlpatterns = [
    # views파일 index함수 호출
    path('',views.index,name='index'),
]
