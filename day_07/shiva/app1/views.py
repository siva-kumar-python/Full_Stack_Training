from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def shiva(request):
    return HttpResponse("Hello, Shiva!\n good morning")

def rakesh(request):
    return HttpResponse("Hello, rakesh!\n good morning")




