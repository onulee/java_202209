from django.urls import path,include
from . import views

app_name="freeBoard"
urlpatterns = [
    path('<int:nowpage>/<str:category>/<str:sword>/fboardList',views.fboardList,name="fboardList"),
    path('<int:nowpage>/<str:category>/<str:sword>/fboardWrite',views.fboardWrite,name="fboardWrite"),
    path('<int:nowpage>/<str:category>/<str:sword>/<str:b_no>/fboardView',views.fboardView,name="fboardView"),
    path('<int:nowpage>/<str:category>/<str:sword>/<str:b_no>/fboardUpdate',views.fboardUpdate,name="fboardUpdate"),
    path('<int:nowpage>/<str:category>/<str:sword>/<str:b_no>/fboardDelete',views.fboardDelete,name="fboardDelete"),
    # 답글쓰기
    path('<int:nowpage>/<str:category>/<str:sword>/<str:b_no>/fboardReply',views.fboardReply,name="fboardReply"),
]
