from django.shortcuts import render,redirect
from member.models import Member

# 회원가입1
def join1(request):
    return render(request,'join01_terms.html')

# 로그아웃
def logout(request):
    request.session.clear()
    return redirect('/')

# 로그인페이지
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("login views : ",id, pw) 
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id'] = qs.id
            request.session['session_name'] = qs.name
            return redirect('/')
        except:    
            context={"msg":'아이디,패스워드가 일치하지 않습니다.'}
            return render(request,'login.html',context)
