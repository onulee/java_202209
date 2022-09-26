from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from member.models import Member

# 회원전체리스트
def memList(request):
    qs = Member.objects.all()
    count = qs.count()
    context={'memList':qs,'count':count}
    return render(request,'memList.html',context)

# 회원상세페이지
def memView(request,m_id):
    qs = Member.objects.get(m_id=m_id)
    context={'mem':qs}
    return render(request,'memView.html',context)

# 회원수정페이지
def memUpdate(request,m_id):
    qs = Member.objects.get(m_id=m_id)
    context={'mem':qs}
    return render(request,'memUpdate.html',context)

# 회원수정저장
def memUpdateOk(request):
    m_id = request.POST.get('id')
    m_pw = request.POST.get('pw')
    m_gender = request.POST.get('gender')
    m_hobby = request.POST.getlist('hobby')
    print('memWrite : ', m_hobby)
    hobby = ','.join(m_hobby)  # list타입 -> str
    print(hobby)
    qs = Member.objects.get(m_id=m_id)
    qs.m_pw = m_pw
    qs.m_gender = m_gender
    qs.m_hobby = hobby
    qs.save()
    return HttpResponseRedirect(reverse('member:memList'))

# 회원정보삭제
def memDelete(request,m_id):
    qs = Member.objects.get(m_id=m_id)
    qs.delete()
    return HttpResponseRedirect(reverse('member:memList'))


# login
def login(request):
    return render(request,'login.html')

# loginOk
def loginOk(request):
    id = request.POST.get('id')
    pw = request.POST.get("pw")
    print("member login : ",id)
    try:
        qs = Member.objects.get(m_id=id,m_pw=pw)
        # 섹션에 저장
        request.session['session_id'] = qs.m_id
        request.session['session_gender'] = qs.m_gender
        print("session end" )
        # id,pw가 틀린경우, 없는 경우
        return redirect("/")
    except:
        context={'msg':"아이디 또는 패스워드가 일치하지 않습니다.\\n다시 로그인 바랍니다."}
        return render(request,'login.html',context)

# logout
def logout(request):
    # session 모두 삭제
    request.session.clear()
    return redirect("/")

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
    
    return HttpResponseRedirect(reverse('member:memList'))