from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a2(request):
    return HttpResponse('<marquee><h1>This is app2 string</h1></marquee>')
def aa2(request):
    return render(request,"aa2.html")