from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def introduction(request):
    return render(request, "info/index.html")
def furkan(request):
    return HttpResponse("Hello, furkan!")
def xd(request):
    return HttpResponse("xd")
def aboutmyself(request):
    return render(request,"info/aboutme.html")