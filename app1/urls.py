from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns=[
    path('football/',football,name='football'),
    path('players/',players,name='players'),
    path('sunil/',sunil,name='sunil'),
    path('neymar/',neymar,name='neymar'),
]
