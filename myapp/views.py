from django.shortcuts import render, redirect
from .forms import ComentarioForm

def home(request):
    return render(request, 'home.html')

def mapa(request):
    return render(request, 'mapa.html')

def reportes(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reportes.html', {'form': ComentarioForm(), 'mensaje': 'Hemos recibido su reporte'})
    else:
        form = ComentarioForm()
    return render(request, 'reportes.html', {'form': form})

def infografia(request):
    return render(request, 'infografia.html')    