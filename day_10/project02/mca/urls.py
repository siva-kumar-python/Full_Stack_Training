from django.urls import path
from .views import StudentCreateView, StudentListView, FacultyCreateView, FacultyListView
from .views import StudentUpdateView, StudentDeleteView,FacultyUpdateView, FacultyDeleteView
urlpatterns = [
    path('student_list', StudentListView.as_view(), name='student_list'),
    path('student_create/', StudentCreateView.as_view(), name='student_create'),
    path('student_update/<int:pk>/', StudentUpdateView.as_view(), name='Student_update'),
    path('student_delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),

    path('faculty_list', FacultyListView.as_view(), name='faculty_list'),
    path('faculty_create/', FacultyCreateView.as_view(), name='faculty_create'),
    path('faculty_update/<int:pk>/', FacultyUpdateView.as_view(), name='faculty_update'),
    path('faculty_delete/<int:pk>/', FacultyDeleteView.as_view(), name='faculty_delete'),
]
