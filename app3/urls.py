from django.urls import path
from app3.views import *
app_name='app3'

urlpatterns=[
    path('marcelo/',marcelo,name='marcelo'),
    path('pele/',pele,name='pele'),
    path('ramos/',ramos,name='ramos'),
]