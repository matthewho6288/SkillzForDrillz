# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello World! Drills for Skills")

def about(request):
    # return HttpResponse("DFS about page")
    return render(request, 'about.html')