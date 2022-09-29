from datetime import datetime
from django.shortcuts import render,redirect
from member.models import Member
from freeBoard.models import Fboard
from django.db.models import F,Q

# 답글쓰기
def fboardReply(request,b_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(b_no=b_no)
        context = {"fboard":qs}
        print("views :",b_no)
        return render(request,'fboardReply.html',context)
    else:
        id = request.session['session_id'] # 현재user id
        member = Member.objects.get(id=id)
        print("views id : ",id)
        b_no = request.POST.get("no")
        b_group = int(request.POST.get("group"))
        b_step = int(request.POST.get("step"))
        b_indent = int(request.POST.get("indent"))
        
        b_title = request.POST.get("title")
        b_content = request.POST.get("content")
        b_file = request.FILES.get('file',None)
        print("views file : ",b_file)
        
        # 같은 그룹에 있는 게시글 전부 step 1씩 증가
              
        
        #저장
        qs = Fboard(member=member,b_title=b_title,b_content=b_content,\
            b_group=b_group,b_step=b_step+1,b_indent=b_indent+1,b_file=b_file)
        qs.save()
        return redirect('freeBoard:fboardList')
    return


# 게시글 검색
def fboardSearch(request):
    category = request.POST.get('category') # all,title,content
    sword = request.POST.get('sword')       # 검색어
    if category=='all':
        qs = Fboard.objects.filter(Q(b_title__contains=sword)|Q(b_content__contains=sword))
    elif category == 'title':
        # content검색
        qs = Fboard.objects.filter(b_title__contains=sword)
    else:
        # content검색
        qs = Fboard.objects.filter(b_content__contains=sword)
    
    context={"fboardList":qs,"category":category,"sword":sword}
    return render(request,'fboardList.html',context)

# 게시판 글삭제
def fboardDelete(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.delete()
    return redirect('freeBoard:fboardList')


# 게시판 업데이트
def fboardUpdate(request,b_no):
    if request.method=='GET':
        qs = Fboard.objects.get(b_no=b_no)
        context = {"fboard":qs}
        print("views :",b_no)
        return render(request,'fboardUpdate.html',context)
    else:
        b_title = request.POST.get('title')
        b_content = request.POST.get('content')
        b_file = request.FILES.get('file',None)
        re_file = request.POST.get('refile')
        print("신규 이미지 : ",b_file)
        print("예전 이미지 : ",re_file)
        qs = Fboard.objects.get(b_no=b_no)
        qs.b_title = b_title
        qs.b_content = b_content
        qs.b_date = datetime.now()
        if b_file:
            qs.b_file=b_file
        qs.save()
        
        return redirect('freeBoard:fboardList')
        

# 게시판뷰
def fboardView(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    context = {"fboard":qs}
    print("views :",b_no)
    return render(request,'fboardView.html',context)


# 게시판리스트
def fboardList(request):
    qs = Fboard.objects.order_by('-b_group','b_step')
    print(qs)
    context={'fboardList':qs}
    return render(request,'fboardList.html',context)

# 게시판글쓰기
def fboardWrite(request):
    if request.method == 'GET':
        return render(request,'fboardWrite.html')
    else:
        id = request.session['session_id']
        print("views id : ",id)
        member = Member.objects.get(id=id)
        b_title = request.POST.get("title")
        b_content = request.POST.get("content")
        b_file = request.FILES.get('file',None)
        print("views file : ",b_file)
        
        #저장
        qs = Fboard(member=member,b_title=b_title,b_content=b_content,b_file=b_file)
        qs.save()
        qs.b_group = qs.b_no
        qs.save()
        return redirect('freeBoard:fboardList')
        
        
