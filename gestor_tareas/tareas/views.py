from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TareaForm


tareas_memoria = {}

@login_required
def lista_tareas(request):
    username = request.user.username
    tareas = tareas_memoria.get(username, [])
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    username = request.user.username
    tareas = tareas_memoria.get(username, [])
    
    tarea = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    
    if tarea is None:
        messages.error(request, 'Tarea no encontrada.')
        return redirect('lista_tareas')
    
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            username = request.user.username
            
            # Inicializar lista de tareas si no existe
            if username not in tareas_memoria:
                tareas_memoria[username] = []
            
            # Calcular nuevo ID
            if tareas_memoria[username]:
                nuevo_id = max(t['id'] for t in tareas_memoria[username]) + 1
            else:
                nuevo_id = 1
            
            # Agregar tarea
            nueva_tarea = {
                'id': nuevo_id,
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion']
            }
            tareas_memoria[username].append(nueva_tarea)
            
            messages.success(request, 'Tarea agregada exitosamente.')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/agregar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    username = request.user.username
    tareas = tareas_memoria.get(username, [])
    
    # Buscar y eliminar la tarea
    tarea_encontrada = False
    for i, tarea in enumerate(tareas):
        if tarea['id'] == tarea_id:
            tareas.pop(i)
            tarea_encontrada = True
            messages.success(request, 'Tarea eliminada exitosamente.')
            break
    
    if not tarea_encontrada:
        messages.error(request, 'Tarea no encontrada.')
    
    return redirect('lista_tareas')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('lista_tareas')
    else:
        form = UserCreationForm()
    
    return render(request, 'tareas/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                return redirect('lista_tareas')
    else:
        form = AuthenticationForm()
    
    return render(request, 'tareas/login.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')