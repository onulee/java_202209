from django.urls import path,include
from . import views

app_name="freeBoard"
urlpatterns = [
    path('<int:nowpage>/fboardList',views.fboardList,name="fboardList"),
    path('fboardWrite',views.fboardWrite,name="fboardWrite"),
    path('<str:b_no>/fboardView',views.fboardView,name="fboardView"),
    path('<str:b_no>/fboardUpdate',views.fboardUpdate,name="fboardUpdate"),
    path('<str:b_no>/fboardDelete',views.fboardDelete,name="fboardDelete"),
    path('fboardSearch',views.fboardSearch,name="fboardSearch"),
    # 답글쓰기
    path('<str:b_no>/fboardReply',views.fboardReply,name="fboardReply"),
]
