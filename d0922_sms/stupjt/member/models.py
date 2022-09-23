from datetime import datetime
from django.db import models

class Member(models.Model):
    m_id = models.CharField(max_length=20)
    m_pw = models.CharField(max_length=100)
    m_gender = models.CharField(max_length=30)
    m_hobby = models.CharField(max_length=100)
    m_date = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.m_id
