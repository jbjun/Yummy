from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass


    def __str__(self):
        return self.id
    
    # 테이블명 지정
    class Meta:
        db_table = 'yummy_member'
        verbose_name = '회원'
        verbose_name_plural = '회원 리스트'