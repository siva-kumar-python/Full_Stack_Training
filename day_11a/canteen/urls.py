from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('cantee/', views.canteen_list, name='canteen_list'),
    path('item/<int:pk>/', views.canteen_detail, name='canteen_detail'),

]