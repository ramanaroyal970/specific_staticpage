from django.urls import path
from app2.views import *
app_name='app2'

urlpatterns=[
    path('messi/',messi,name='messi'),
    path('kmbappae/',kmbappae,name='kmbappae'),
    path('levendoski/',levendoski,name='levendoski'),
    path('maradona/',maradona,name='maradona'),
    path('zaltan/',zaltan,name='zaltan'),
    
]
