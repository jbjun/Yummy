from django.shortcuts import render

def list(request):
    return render(request,'list.html')

def detail(request):
    return render(request,'detail.html')