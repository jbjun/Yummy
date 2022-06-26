from django import forms
from django.contrib.auth import get_user_model
import re
from django.forms import ValidationError

User = get_user_model()

REGEX_EMAIL        = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD     = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

class SignupForm(forms.Form):
    # firstname = forms.CharField(max_length=30, label='First name')
    # lastname = forms.CharField(max_length=30, label='Last name')


    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',

            }

        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # 성 확인을 위한 필드
    email = forms.CharField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    # 성 확인을 위한 필드
    firstname = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    # 이름 확인을 위한 필드
    lastname = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # username필드의 검증에 username이 이미 사용중인지 여부 검사
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다')
        return username

    def clean_password1(self):
          password1 = self.cleaned_data['password1']
          if not re.match(REGEX_PASSWORD, password1):
              raise ValidationError("비밀번호 양식이 맞지 않습니다.")
          return password1

    def clean_email(self):
         email = self.cleaned_data['email']
         if not re.match(REGEX_EMAIL, email):
                 raise ValidationError("이메일 형식이 아닙니다.")
         return email


  #자신이 가진 username과 password를 사용해서 유저 생성 후 반환하는 메서드
    def signup(self):
         if self.is_valid():
             username = self.cleaned_data['username']
             password = self.cleaned_data['password1']
             email = self.cleaned_data['email']
             firstname = self.cleaned_data['firstname']
             lastname = self.cleaned_data['lastname']

             user = User.objects.create_user(username,email,password)
             user.first_name = firstname
             user.last_name = lastname
             user.save()

             return user
