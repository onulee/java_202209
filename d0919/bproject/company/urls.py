from . import views
from django.urls import path,include

app_name='company'
urlpatterns = [
    path('ceo/',views.ceo,name='ceo'),
    path('philosophy/',views.philosophy,name='philosophy'),
]



