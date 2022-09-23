from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from member.models import Member

# login
def login(request):
    return render(request,'login.html')


# 회원정보페이지 호출
def memWrite(request):
    return render(request,'memWrite.html')

# 회원정보 저장
def memWriteOk(request):
    m_id = request.POST.get('id')
    m_pw = request.POST.get('pw')
    m_gender = request.POST.get('gender')
    m_hobby = request.POST.getlist('hobby')
    print('memWrite : ', m_hobby)
    hobby = ','.join(m_hobby)  # list타입 -> str
    print(hobby)
    qs = Member(m_id=m_id,m_pw=m_pw,m_gender=m_gender,m_hobby=hobby)
    qs.save()
    
    return HttpResponseRedirect(reverse('index'))