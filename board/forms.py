from django import forms
from .models import Board

from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextField


class BoardWriteForm(forms.ModelForm):

    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '게시글 제목'
            }),
        required=True,
    )

    contents = SummernoteTextField

    options = (
        ('test1', 'test1 게시판'),
        ('test2', 'test2 게시판')
    )

    board_name = forms.ChoiceField(
        label='게시판 선택',
        widget=forms.Select(),
        choices=options
    )

    field_order = [
        'title',
        'board_name',
        'contents'
    ]

    class Meta:
        model = Board
        fields = [
            'writer',
            'title',
            'image',
            'contents',


            'board_name'

        ]
        widgets = {
            'contents' : SummernoteWidget()
        }

    def celan(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title','')
        contents = cleaned_data.get('contests','')
        board_name = cleaned_data.get('board_name','Python')

        if title == '':
            self.add_error('title','글 제목을 입력하세요.')
        elif contents == '':
            self.add_error('contents','글 내용을 입력하세요')
        else:
            self.title = title
            self.contents = contents
            self.board_name = board_name