from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.home,name ='home'),
    path('app/',views.app,name ='app'),
    path('jss/',views.jss,name ='jss'),
    path('jss1/',views.jss1,name ='jss1'),
   
    
]