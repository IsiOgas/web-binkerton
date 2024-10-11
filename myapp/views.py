from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello world!</h1>")

def mapa(request):
    return HttpResponse('mapa')

def reportes(request):
    return HttpResponse('reportes')