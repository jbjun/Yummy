from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def detail(request):
    return render(request,'detail.html')

#브랜치 테스트 주석입니다