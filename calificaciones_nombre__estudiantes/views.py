from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('calificaciones:listar_calificaciones')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calificaciones:listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear.html', {'form': form})

@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    promedio_general = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    if promedio_general is not None:
        promedio_general = round(promedio_general, 2)
    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general
    })

@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('calificaciones:listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar.html', {'form': form})

@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones:listar_calificaciones')
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})

@login_required
def promedio_general(request):
    promedio = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    if promedio is not None:
        promedio = round(promedio, 2)
    return render(request, 'calificaciones/promedio_general.html', {'promedio_general': promedio})
