from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    temp=loader.get_template('login.html')
    return HttpResponse(temp.render())


def app(request):
    temp=loader.get_template('app.html')
    return HttpResponse(temp.render())

def jss(request):
    temp=loader.get_template('js02.html')
    return HttpResponse(temp.render())

def jss1(request):
    temp=loader.get_template('shiva.html')
    return HttpResponse(temp.render())