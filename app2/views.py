from django.shortcuts import render

# Create your views here.

def messi(request):
    return render(request,'messi.html')

def kmbappae(request):
    return render(request,'kmbappae.html')

def levendoski(request):
    return render(request,'levendoski.html')

def maradona(request):
    return render(request,'maradona.html')

def zaltan(request):
    return render(request,'zaltan.html')