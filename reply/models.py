from django.db import models

# Create your models here.
class Board(models.Model):
    
    writer = models.CharField(max_length=64,
                                verbose_name='작성자')
    content = models.CharField(max_length=1000,
                                verbose_name='내용')
    reg_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록일자')


    def __str__(self):
        return self.writer
    
    # 테이블명 지정
    class Meta:
        db_table = 'yummy_board_reply'
        verbose_name = '리뷰 게시판_댓글'
        verbose_name_plural = '리뷰 게시판_댓글'
