from django.shortcuts import render

# index함수 선언
def index(request):
    # render : html페이지 열어줌 
    return render(request,'index.html')
