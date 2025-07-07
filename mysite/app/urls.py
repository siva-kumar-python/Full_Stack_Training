from django.urls import path 
from . import views

urlpatterns= [
    path('abc/',views.abc,name='abc'),
    path('',views.shiva,name='shiva'),
]