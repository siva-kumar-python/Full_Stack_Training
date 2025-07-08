from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('dms/',views.dms,name='dms'),
    path('java/',views.java,name='java'),
    path('os/',views.os,name='os'),
    path('co/',views.co,name='co'),
    path('afm/',views.afm,name='afm'),
    path('coor/',views.coor,name='coor'),
    path('dccn/',views.dccn,name='dccn'),
    path('dsa/',views.dsa,name='dsa'),
    path('adbms/',views.adbms,name='adbms'),
    path('ecommers/',views.ecommers,name='ecommers'),
]