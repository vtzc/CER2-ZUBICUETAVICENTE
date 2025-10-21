from django.shortcuts import render

from .models import Evento  
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def mis_eventos(request):
    eventos_inscritos = request.user.eventos_inscritos.all()
    return render(request, 'core/mis_eventos.html', {'eventos': eventos_inscritos})

@login_required
def inscribir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if evento.plazas_disponibles > 0 and request.user not in evento.asistentes.all():
        evento.asistentes.add(request.user)
        evento.plazas_disponibles -= 1
        evento.save()
        messages.success(request, f'Te has inscrito exitosamente en "{evento.titulo}" ')
    else:
        messages.error(request, 'No hay plazas disponibles o ya estás inscrito en este evento.')
    return redirect('eventos')

@login_required
def anular_inscripcion(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.user in evento.asistentes.all():
        evento.asistentes.remove(request.user)
        evento.plazas_disponibles += 1
        evento.save()
        messages.success(request, f'Has anulado tu inscripción para "{evento.titulo}".')
    else:
        messages.error(request, 'No estabas inscrito en este evento.')
    return redirect('mis_eventos')