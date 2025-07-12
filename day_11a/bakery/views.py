from django.shortcuts import render,get_object_or_404
from .models import Bakery
# Create your views here.

def bakery_list(request):
    obj_all = Bakery.objects.all()
    return render(request, 'bakery_list.html', {'bakerys': obj_all})

def bakery_detail(request, pk):
    obj = get_object_or_404(Bakery, pk=pk)
    return render(request, 'Bakery_detail.html', {'bakery': obj})

def home(request):
    return render(request, 'home.html')

