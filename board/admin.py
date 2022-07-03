from django.contrib import admin
from .models import Board, Reply


class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writer',
        'hits',
        'reg_date',
        )
    search_fields = ('title', 'content', 'writer__user_id',)

class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'contents',
        'writer',
        'created',
        'deleted',
    )
    search_fields = ('post__title', 'contents', 'writer__user_id',)

admin.site.register(Board, BoardAdmin)
admin.site.register(Reply, ReplyAdmin)
