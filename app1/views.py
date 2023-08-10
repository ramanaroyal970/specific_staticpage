from django.shortcuts import render

# Create your views here.
def football(request):
    return render(request,'football.html')


def players(request):
    return render(request,'players.html')

def sunil(request):
    return render(request,'sunil.html')

def neymar(request):
    return render(request,'neymar.html')

