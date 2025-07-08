from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def abc(request):
    return HttpResponse("dhsdytfauyghsauiohDAHBKEDGUS")


def shiva(request):
    temp=loader.get_template('app.html')
    return HttpResponse(temp.render())