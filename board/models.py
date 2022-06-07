from sqlite3 import register_adapter
from django.db import models

# Create your models here.
class Board(models.Model):
    writer = models.ForeignKey('member.Member', on_delete=models.CASCADE,
                                verbose_name='작성자')
    title = models.CharField(max_length=64,
                                verbose_name='제목')
    content = models.TextField(max_length=64,
                                verbose_name='내용')
    reg_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록일자')
    update_date = models.DateTimeField(auto_now_add=False,
                                        verbose_name='수정일자')
    delete_date = models.DateTimeField(auto_now_add=False,
                                        verbose_name='삭제일자')


    def __str__(self):
        return self.title
    
    # 테이블명 지정
    class Meta:
        db_table = 'yummy_board'
        verbose_name = '리뷰 게시판'
        verbose_name_plural = '리뷰 게시판'
