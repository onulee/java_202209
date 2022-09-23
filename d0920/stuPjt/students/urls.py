from django.urls import path, include
from . import views

app_name='students'
urlpatterns = [
    path('stuWrite/',views.stuWrite, name='stuWrite'),
]
