from django.urls import path
from . import views

urlpatterns=[
    path('bakery_list/',views.bakery_list,name='bakery_list'),
    path('bakery_details/<int:pk>/',views.bakery_detail,name='bakery_ditails'),
]