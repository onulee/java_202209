from datetime import datetime
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from students.models import Student



# 학생전체리스트
def stuList(request):
    qs = Student.objects.all()
    # qs = Student.objects.order_by('-s_no') #역순정렬
    count = qs.count() # 학생전체리스트 개수
    context = {'stuList':qs, 'count':count } #dic타입으로 전송
    return render(request,'stuList.html',context)

# 학생상세페이지 호출
def stuView(request,s_no):
    print("학생상세페이지 : "+s_no)
    qs = Student.objects.get(s_no=s_no)
    context ={'stu':qs}
    return render(request,'stuView.html',context)

# 학생등록페이지 호출
def stuWrite(request):
    return render(request,'stuWrite.html')

# 학생정보 저장
def stuWriteOk(request):
    s_name = request.POST.get('name')
    s_major = request.POST.get('major')
    s_age = request.POST.get('age')
    s_grade = request.POST.get('grade')
    s_gender = request.POST.get('gender')
    print("views : "+s_name)
    qs = Student(s_name=s_name,s_major=s_major,s_age=s_age,s_grade=s_grade,s_gender=s_gender)
    qs.save()
    
    print("write Ok!!")
    
    return HttpResponseRedirect(reverse('students:stuList'))

# 학생정보수정 페이지 호출
def stuUpdate(request,s_no):
    print("stuUpdate : "+s_no)
    qs = Student.objects.get(s_no=s_no)
    context={'stu':qs}
    # 학생정보 1명
    return render(request,'stuUpdate.html',context)

# 학생정보수정 저장
def stuUpdateOk(request):
    s_no = request.POST.get('no')
    s_major = request.POST.get('major')
    s_age = request.POST.get('age')
    s_grade = request.POST.get('grade')
    s_gender = request.POST.get('gender')
    print("stuUpdateOk : "+s_no)
    qs = Student.objects.get(s_no=s_no)
    qs.s_major = s_major
    qs.s_age = s_age
    qs.s_grade = s_grade
    qs.s_gender = s_gender
    qs.s_date = datetime.now()
    qs.save()
    print("update Ok!!")
    
    return HttpResponseRedirect(reverse('students:stuList'))

# 학생정보 삭제
def stuDelete(request,s_no):
    print("stuDelete : "+ s_no)
    qs = Student.objects.get(s_no=s_no)
    qs.delete()
    return HttpResponseRedirect(reverse('students:stuList'))
    

