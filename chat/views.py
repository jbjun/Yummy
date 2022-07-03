from django.shortcuts import render

def chatt(request):
    return render(request, 'chatt.html')

def room(request):
    return render(request, 'room.html')