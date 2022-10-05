from datetime import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from member.models import Member

class Fboard(models.Model):
    # 번호
    b_no = models.AutoField(primary_key=True)
    # 작성자
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    # 제목
    b_title = models.CharField(max_length=1000)
    # 내용
    b_content = models.TextField()
    # 작성일
    b_date = models.DateTimeField(default=datetime.now(),blank=True)
    # 답글 group
    b_group = models.IntegerField(default=0)
    # group 순서를 정함
    b_step = models.IntegerField(default=0)
    # 들여쓰기
    b_indent = models.IntegerField(default=0)
    # 조회수
    b_hit = models.IntegerField(default=1)
    # 파일첨부
    b_file = models.ImageField(blank=True)
    
    def __str__(self):
        return self.b_title
    
# 하단댓글DB    
class Comment(models.Model):    
    c_no = models.AutoField(primary_key=True)
    # member가 삭제되면 그대로 존재
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
    # fboard가 삭제되면 모두 삭제
    fboard = models.ForeignKey(Fboard,on_delete=models.CASCADE)
    c_pw = models.CharField(max_length=10,blank=True)
    c_content = models.TextField()
    c_date = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.c_content
