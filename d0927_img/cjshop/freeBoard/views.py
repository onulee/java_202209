from django.shortcuts import render,redirect
from member.models import Member
from freeBoard.models import Fboard

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
        id = request.POST.get("id")
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
        
        
