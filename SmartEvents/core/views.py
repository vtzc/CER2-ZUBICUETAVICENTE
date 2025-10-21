from django.shortcuts import render
from .models import Evento

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def eventos(request):
    lista_eventos = Evento.objects.all()
    context = {'eventos': lista_eventos} 
    return render(request, 'core/eventos.html')

def comunidad(request):   
    return render(request, 'core/comunidad.html')

