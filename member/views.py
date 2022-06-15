import django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else:
            print("인증실패")
        
    return render(request,"member/login.html")

def logout_view(request):

    logout(request)

    return redirect("member:login")