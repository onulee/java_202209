from datetime import datetime
from django.db import models

class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_title = models.CharField(max_length=300)
    b_content = models.TextField()
    b_hit = models.IntegerField(default=0)
    b_date = models.DateTimeField(default=datetime.now(),blank=False)
    
    def __str__(self):
        return self.b_title
