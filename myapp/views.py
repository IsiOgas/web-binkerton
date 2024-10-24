from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def mapa(request):
    return render(request, 'mapa.html')

def reportes(request):
    return render(request, 'reportes.html')