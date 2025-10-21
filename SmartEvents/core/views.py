from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def eventos(request):
    return render(request, 'core/eventos.html')

def comunidad(request):   
    return render(request, 'core/comunidad.html')

