from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.BoardListView.as_view(), name='board_list'),
    path('<int:pk>/', views.board_detail_view, name='board_detail'),
    path('write/', views.board_write_view, name='board_write'),
    path('<int:pk>/edit/', views.board_edit_view, name='board_edit'),
    path('<int:pk>/delete/', views.board_delete_view, name='board_delete'),
    path('<int:pk>/reply/write/', views.reply_write_view, name='reply_write'),
    path('<int:pk>/reply/delete/', views.reply_delete_view, name='reply_delete'),
]
