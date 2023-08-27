from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def introduction(request):
    return render(request, "info/index.html")
def aboutmyself(request):
    return render(request,"info/about.html")