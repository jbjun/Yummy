from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=64,
                                verbose_name='아이디')
    pw = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    zipcode = models.CharField(max_length=64,
                                verbose_name='우편번호')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    address = models.CharField(max_length=64, verbose_name='주소')
    address_detail = models.CharField(max_length=64, verbose_name='상세주소')
    picture = models.CharField(max_length=100, verbose_name='사진파일이름')


    def __str__(self):
        return self.id
    
    # 테이블명 지정
    class Meta:
        db_table = 'yummy_member'
        verbose_name = '회원'
        verbose_name_plural = '회원 리스트'
