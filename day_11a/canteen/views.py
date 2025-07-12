from django.shortcuts import render,get_object_or_404
from .models import Canteen
# Create your views here.

def canteen_list(request):
    obj_all = Canteen.objects.all()
    return render(request, 'canteen_list.html', {'canteens': obj_all})

def canteen_detail(request, pk):
    obj = get_object_or_404(Canteen, pk=pk)
    return render(request, 'canteen_detail.html', {'canteen': obj})

def home(request):
    return render(request, 'home.html')