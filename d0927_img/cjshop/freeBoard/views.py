from datetime import datetime
from django.shortcuts import render,redirect
from member.models import Member
from freeBoard.models import Comment, Fboard, Revenue
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import requests


# 차트그리기
def chart01(request):
    return render(request,'chart01.html')

# 차트-json
@csrf_exempt
def chartData(request):
    qs = Revenue.objects.all()
    chartList = list(qs.values())
    print("views chartData : ")
    print(chartList)
    
    return JsonResponse(chartList,safe=False)

@csrf_exempt
def chartList(request):
    public_key ='918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    resultType ='json'
    url = 'http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={}&numOfRows=10&pageNo=1&resultType={}'.format(public_key,resultType)
    res = requests.get(url)  # url에 있는 소스 코드 가져오기
    json_res = json.loads(res.text) # 모든 소스코드, json타입으로 변경
    publicList = json_res['response']['body']['items']
    # nlist = list(map(int,publicList)) #dic타입을 list타입으로 변경
    # nlist = list(publicList) #dic타입을 list타입으로 변경
    nlist =[1,2,3,4,5]
    
    print("nlist")
    print(publicList)
    
    return JsonResponse(publicList,safe=False)


# 공공데이터 리스트
def publicList(request):

    public_key ='918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    resultType ='json'
    url = 'http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={}&numOfRows=10&pageNo=1&resultType={}'.format(public_key,resultType)
    res = requests.get(url)  # url에 있는 소스 코드 가져오기
    json_res = json.loads(res.text) # 모든 소스코드, json타입으로 변경
    publicList = json_res['response']['body']['items']['item']
    numOfRows = json_res['response']['body']['numOfRows']
    # nlist = list(map(int,numOfRows)) #dic타입을 list타입으로 변경
    # nlist = list(numOfRows) #dic타입을 list타입으로 변경
    
    print("numOfRows : ",numOfRows)
    print("publicList")
    print(publicList)
    context={'publicList':publicList,"numOfRows":numOfRows}
    
    
    
    return render(request,'publicList.html',context)



# post방식 테스트
@csrf_exempt
def commPost(request):
    test = request.POST.get("test")
    print(test)
    context = {"msg":"데이터전송이 잘되었습니다." }
    return JsonResponse(context)


# 댓글삭제
def commDelete(request):
    c_no = request.GET.get('c_no')
    qs = Comment.objects.get(c_no=c_no)
    qs.delete()
    context={'msg':"댓글이 삭제되었습니다."}
    return JsonResponse(context)


# 댓글수정저장
def commUpdate(request):
    # 데이터 가져오기
    c_no = request.GET.get('c_no')
    c_content = request.GET.get('c_content')
    id = request.session.get('session_id')
    print("views commUpdate : ",c_content)
    # 검색 및 저장
    qs = Comment.objects.get(c_no=c_no)
    qs.c_content = c_content
    qs.c_date = datetime.now()
    qs.save()
    
    # 저장데이터 보내기
    context={"c_no":c_no,"c_content":c_content,"c_date":qs.c_date}
    return JsonResponse(context)
    

# 댓글쓰기 - ajax
def commWrite(request):
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    b_no = request.GET.get('b_no')
    fboard = Fboard.objects.get(b_no=b_no)
    c_pw = request.GET.get('c_pw')
    c_content = request.GET.get('c_content')
    
    # 데이터저장
    qs = Comment(member=member,fboard=fboard,c_pw=c_pw,c_content = c_content)
    qs.save()
    # 필요데이터 가져오기
    c_no = qs.c_no
    c_date = qs.c_date
    
    # 저장데이터 보내기
    context={"c_no":c_no,"b_no":b_no,"c_pw":c_pw,"c_content":c_content,"c_date":c_date}
    return JsonResponse(context) 
    

# 댓글리스트 - ajax
def commList(request):
    b_no = request.GET.get('b_no')
    print("views commList b_no : ",b_no)
    comm_qs = Comment.objects.filter(fboard=b_no).order_by('-c_no')
    # list타입으로 전송 : safe=False
    clist = list(comm_qs.values()) 
    print(clist)
    
    return JsonResponse(clist,safe=False)
    


# event
def event(request):
    qs = Fboard.objects.order_by('-b_group','b_step')  #모두 검색
    
    # 하단페이지 분기    
    paginator = Paginator(qs,3)  # qs/10 총하단페이지 수 
    qs = paginator.get_page(1)  # 3페이지 게시글을 보내줌.
    
    context={"fboardList":qs}
    return render(request,'event.html',context)

# eventView
def eventView(request,b_no):
    # request.GET.get('b_no')
    # 게시글 1개 가져오기
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_hit += 1     # 조회수 1증가
    qs.save()
    # 게시글에 해당되는 하단댓글 모두 가져오기
    comm_qs = Comment.objects.filter(fboard=b_no).order_by('-c_no')
    count = comm_qs.count()
    context = {"fboard":qs,"commList":comm_qs,"commCount":count}
    return render(request,'eventView.html',context)

# 답글쓰기
def fboardReply(request,nowpage,category,sword,b_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(b_no=b_no)
        context = {"fboard":qs,"nowpage":nowpage,"category":category,"sword":sword}
        print("views :",b_no)
        return render(request,'fboardReply.html',context)
    else:
        id = request.session['session_id'] # 현재user id
        member = Member.objects.get(id=id)
        print("views id : ",id)
        b_no = request.POST.get("no")
        b_group = int(request.POST.get("group"))   # 부모의 group
        b_step = int(request.POST.get("step"))     # 부모의 step
        b_indent = int(request.POST.get("indent")) # 부모의 indent
        
        b_title = request.POST.get("title")
        b_content = request.POST.get("content")
        b_file = request.FILES.get('file',None)
        print("views file : ",b_file)
        
        # 부모의 step보다 큰수는 모두 +1을 해야 함.
        Fboard.objects.filter(b_group=b_group,b_step__gt=b_step).update\
            (b_step=F('b_step')+1)
        
        # reboard = Fboard.objects.filter(b_group=b_group,b_step__gt=b_step)
        # reboard.update(b_step=F('b_step')+1)
        
        # 저장 - 부모의 group같아야 함, step+1, indent+1
        qs = Fboard(member=member,b_title=b_title,b_content=b_content,\
            b_group=b_group,b_step=b_step+1,b_indent=b_indent+1,b_file=b_file)
        qs.save()
        return redirect('freeBoard:fboardList', nowpage,category,sword)
    return




# 게시판 글삭제
def fboardDelete(request,nowpage,category,sword,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.delete()
    return redirect('freeBoard:fboardList', nowpage,category,sword)


# 게시판 업데이트
def fboardUpdate(request,nowpage,category,sword,b_no):
    if request.method=='GET':
        qs = Fboard.objects.get(b_no=b_no)
        context = {"fboard":qs,"nowpage":nowpage,"category":category,"sword":sword}
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
        
        return redirect('freeBoard:fboardList', nowpage,category,sword)
        

# 게시판뷰
def fboardView(request,nowpage,category,sword,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_hit += 1     # 조회수 1증가
    qs.save()
    print("views :",b_no)
    
    # 이전글
    try:
        # 답글이 달려 있을때
        qs_prev = Fboard.objects.filter(b_group=qs.b_group,b_step__lt=qs.b_step).order_by('-b_group','b_step').last().b_no
    except:
        # 답글이 아닌경우
        try:
            qs_prev = Fboard.objects.filter(b_group__gt=qs.b_group).order_by('-b_group','b_step').last().b_no
        except:
            # 마지막번호 클릭시 last가 없을때
            qs_prev = Fboard.objects.order_by('-b_group','b_step').first().b_no
    
    print("qs_prev : ",qs_prev)
    
    # 다음글
    try:
        qs_next = Fboard.objects.filter(b_group=qs.b_group,b_step__gt=qs.b_step).order_by('-b_group','b_step').first().b_no
    except:
        try:
            qs_next = Fboard.objects.filter(b_group__lt=qs.b_group).order_by('-b_group','b_step').first().b_no
        except:
            qs_next = Fboard.objects.order_by('-b_group','b_step').last().b_no    
    
    print("qs_next : ",qs_next)
    
    # 이전글,다음글 데이터 불러오기
    qsPrevData = Fboard.objects.get(b_no=qs_prev)
    qsNextData = Fboard.objects.get(b_no=qs_next)
    
    context = {"fboard":qs,'fboardPrev':qsPrevData,'fboardNext':qsNextData,'nowpage':nowpage,"category":category,"sword":sword}
    return render(request,'fboardView.html',context)


### 게시판리스트
def fboardList(request,nowpage,category,sword):
    # 1. 게시판리스트페이지가 호출되어 넘어온 1페이지 - 검색어 공백
    # 2. 게시판리스트페이지에서 넘어온 2페이지 - 검색어 공백
    # 3. 검색을 해서 넘어온 1페이지 - 검색어 있음
    # 4. 검색을 해서 넘어온 2페이지 - 검색어 있음
    print("view List : ",nowpage,category,sword)
    
    # 게시판리스트 호출 - 검색버튼 클릭해서 넘어온 페이지
    if request.method == "POST":
       ncategory = request.POST.get('category') # all,title,content
       nsword = request.POST.get('sword')       # 검색어
       category = ncategory
       sword = nsword
    
    # db 게시글 호출   
    if category=='1' and sword =='1':
        qs = Fboard.objects.order_by('-b_group','b_step')  #모두 검색
    else:
        if category=='all':
            qs = Fboard.objects.filter(Q(b_title__contains=sword)|Q(b_content__contains=sword))
        elif category == 'title':
            # content검색
            qs = Fboard.objects.filter(b_title__contains=sword)
        else:
            # content검색
            qs = Fboard.objects.filter(b_content__contains=sword)
    
    # 하단페이지 분기    
    paginator = Paginator(qs,10)  # qs/10 총하단페이지 수 
    qs = paginator.get_page(nowpage)  # 3페이지 게시글을 보내줌.
    
    context={"fboardList":qs,"category":category,"sword":sword,"nowpage":nowpage}
    return render(request,'fboardList.html',context)     
        


# 게시판글쓰기
def fboardWrite(request,nowpage,category,sword,):
    # write페이지 호출
    if request.method == 'GET':
        context={"nowpage":nowpage,"category":category,"sword":sword}
        return render(request,'fboardWrite.html',context)
    else:
        id = request.session['session_id'] # session가져오기
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
        return redirect('freeBoard:fboardList', nowpage,category,sword)
        
        
