from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writer',
        'hits',
        'reg_date',
        )
    search_fields = ('title', 'content', 'writer__user_id',)

admin.site.register(Board, BoardAdmin)