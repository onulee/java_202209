from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student

# 학생등록페이지
def stuWrite(request):
    if request.method == 'GET':
        return render(request,'stuWrite.html')
    else:
        print("method : ",request.method)
        s_name = request.POST.get('name')
        s_major = request.POST.get('major')
        s_age = request.POST.get('age')
        s_grade = request.POST.get('grade')
        s_gender = request.POST.get('gender')
        print(s_name,s_major,s_age,s_grade,s_gender)
    
        # 학생전체리스트 이동
        return HttpResponseRedirect(reverse('index'))
        

# 학생등록저장
def stuWriteOk(request):
    print("method : ",request.method)
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))
    s_name = request.POST.get('name')
    s_major = request.POST.get('major')
    s_age = request.POST.get('age')
    s_grade = request.POST.get('grade')
    s_gender = request.POST.get('gender')
    print(s_name,s_major,s_age,s_grade,s_gender)
    
    # 데이터 저장 1
    qs = Student(s_name=s_name,s_major=s_major,s_age=s_age,s_grade=s_grade,s_gender=s_gender)
    qs.save()
    # 데이터 저장 2
    # Student.objects.create(s_name=s_name,s_major=s_major,s_age=s_age,s_grade=s_grade,s_gender=s_gender)
    
    # 학생전체리스트 이동
    return HttpResponseRedirect(reverse('index'))
