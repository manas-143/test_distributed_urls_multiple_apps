from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a1(request):
    return HttpResponse('<marquee><h1>This is app1 string</h1></marquee>')
def aa1(request):
    return render(request,"aa1.html")