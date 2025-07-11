from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import StudentModel,FacultyModel

# Create your views here.
#fro student add
class StudentCreateView(CreateView):
    model=StudentModel
    fields=['roll_no','name','course','marks']
    success_url=reverse_lazy('student_list')
#fro faculty add
class FacultyCreateView(CreateView):
    model=FacultyModel
    fields=['id','name','subject']
    success_url=reverse_lazy('faculty_list')
# for student view records
class StudentListView(ListView):
    model=StudentModel

#for faculty view all records 

class FacultyListView(ListView):
    model=FacultyModel

class StudentUpdateView(UpdateView):
    model =StudentModel
    fields = ['roll_no','name','course','marks']
    success_url = reverse_lazy('student_list')

class FacultyUpdateView(UpdateView):
    model =FacultyModel
    fields = ['id','name','subject']
    success_url = reverse_lazy('faculty_list')

class StudentDeleteView(DeleteView):
    model = StudentModel
    success_url = reverse_lazy('student_list') 
    

class FacultyDeleteView(DeleteView):
    model = FacultyModel
    success_url = reverse_lazy('faculty_list') 