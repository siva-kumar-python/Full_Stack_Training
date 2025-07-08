from django.urls import path

from . import views


urlpatterns=[
    path('shiva/',views.shiva,name ='shiva'),
    path('rakesh/',views.rakesh,name ='rakesh'),

    
]