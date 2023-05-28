from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a3(request):
    return HttpResponse('<marquee><h1>This is app3 string</h1></marquee>')
def aa3(request):
    return render(request,"aa3.html")