from django.shortcuts import render

# ceo페이지 호출
def ceo(request):
    return render(request,'ceo.html')

def philosophy(request):
    return render(request,'philosophy.html')
