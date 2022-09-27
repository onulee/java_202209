from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('join1/',views.join1, name='join1'),
]
