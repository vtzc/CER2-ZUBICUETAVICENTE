from django.shortcuts import render

from .models import Evento  
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect 

# Create your views here.

def home(request):
    eventos_proximos = Evento.objects.filter(fecha_hora__gte=timezone.now()).order_by('fecha_hora')[:3]
    context = {'eventos': eventos_proximos}
    return render(request, 'core/home.html', context)

def eventos(request):
    lista_eventos = Evento.objects.all()
    context = {'eventos': lista_eventos}
    return render(request, 'core/eventos.html', context)

def comunidad(request):   
    return render(request, 'core/comunidad.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')