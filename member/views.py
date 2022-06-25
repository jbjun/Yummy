from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from django.core.exceptions import ValidationError
from .forms import SignupForm

# Create your views here.

#
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             print("인증성공")
#             login(request,user)
#             return render(request, "index.html")
#         else:
#             print("인증실패")
#
#     return render(request,"member/login.html")
#
# def logout_view(request):
#
#     logout(request)
#
#     return redirect("member:login")
#
#
# def signup_view(request):
#     if request.method == 'POST':
#         signup_form = SignupForm(request.POST)
#         # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
#         if signup_form.is_valid():
#             # SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
#             signup_form.signup()
#             return redirect("member:login")
#     else:
#         signup_form = SignupForm()
#
#     context = {
#         'signup_form': signup_form,
#     }
#     return render(request, 'member/signup.html', context)