from django.shortcuts import render

# Create your views here.
def marcelo(request):
    return render(request,'marcelo.html')

def pele(request):
    return render(request,'pele.html')

def ramos(request):
    return render(request,'ramos.html')

