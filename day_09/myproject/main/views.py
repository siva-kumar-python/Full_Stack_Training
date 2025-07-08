from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())

def dms(request):
    temp=loader.get_template('dms.html')
    return HttpResponse(temp.render())

def java(request):
    temp=loader.get_template('java.html')
    return HttpResponse(temp.render())

def os(request):
    temp=loader.get_template('os.html')
    return HttpResponse(temp.render())
def co(requet):
    temp=loader.get_template('co.html')
    return HttpResponse(temp.render())

def afm(requet):
    temp=loader.get_template('afm.html')
    return HttpResponse(temp.render())

def coor(requet):
    temp=loader.get_template('coor.html')
    return HttpResponse(temp.render())

def dccn(requet):
    temp=loader.get_template('dccn.html')
    return HttpResponse(temp.render())

def dsa(requet):
    temp=loader.get_template('dsa.html')
    return HttpResponse(temp.render())

def adbms(requet):
    temp=loader.get_template('adbms.html')
    return HttpResponse(temp.render())

def ecommers(requet):
    temp=loader.get_template('ecommers.html')
    return HttpResponse(temp.render())


