from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from .models import Vehiculo, Vivienda

def es_administrador(usuario):
    return usuario.is_staff or usuario.is_superuser or getattr(getattr(usuario, 'perfil', None), 'cargo', '') == 'administrador'

administrador_requerido = user_passes_test(es_administrador, login_url='/comunidad/login/')

def iniciar_sesion(request):
    error = None
    if request.method == 'POST':
        usuario = authenticate(request, username=request.POST.get('usuario'), password=request.POST.get('contrasena'))
        tipo = request.POST.get('tipo_usuario', 'usuario')
        es_admin = usuario is not None and (usuario.is_staff or usuario.is_superuser)
        es_usuario = usuario is not None and hasattr(usuario, 'perfil') and usuario.perfil.cargo != 'administrador'
        if usuario is not None and ((tipo == 'administrador' and es_admin) or (tipo == 'usuario' and es_usuario)):
            login(request, usuario)
            if tipo == 'administrador':
                return redirect('comunidad')
            return redirect('inicio')
        error = 'Credenciales incorrectas o tipo de acceso no autorizado.'
    return render(request, 'registration/login.html', {'error': error})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def inicio(request):
    return render(request, 'core/inicio.html', {'viviendas': Vivienda.objects.prefetch_related('vehiculos'), 'vehiculos': Vehiculo.objects.select_related('vivienda')})

@login_required
def dashboard_comunidad(request):
    return render(request, 'core/dashboard_comunidad.html', {'cantidad_viviendas': Vivienda.objects.count(), 'cantidad_vehiculos': Vehiculo.objects.count()})

@login_required
def lista_vehiculos(request):
    return render(request, 'core/lista_vehiculos.html', {'vehiculos': Vehiculo.objects.select_related('vivienda')})

@administrador_requerido
def crear_vivienda(request):
    if request.method == 'POST':
        Vivienda.objects.create(piso=request.POST['piso'], numero=request.POST['numero'], propietario=request.POST['propietario'])
        messages.success(request, 'La vivienda fue creada correctamente.')
        return redirect('inicio')
    return render(request, 'core/formulario_vivienda.html', {'titulo': 'Crear vivienda'})

@login_required
def detalle_vivienda(request, identificador_vivienda):
    vivienda = Vivienda.objects.prefetch_related('vehiculos').get(id=identificador_vivienda)
    return render(request, 'core/detalle_vivienda.html', {'vivienda': vivienda})

@administrador_requerido
def crear_vehiculo(request, identificador_vivienda):
    vivienda = Vivienda.objects.get(id=identificador_vivienda)
    if request.method == 'POST':
        Vehiculo.objects.create(vivienda=vivienda, patente=request.POST['patente'].upper(), marca=request.POST.get('marca', ''), modelo=request.POST.get('modelo', ''), color=request.POST.get('color', ''))
        messages.success(request, 'El vehículo fue añadido a la vivienda.')
        return redirect('detalle-vivienda', identificador_vivienda=vivienda.id)
    return render(request, 'core/formulario_vehiculo.html', {'vivienda': vivienda})

@administrador_requerido
def editar_vivienda(request, identificador_vivienda):
    vivienda = Vivienda.objects.get(id=identificador_vivienda)
    if request.method == 'POST':
        vivienda.piso = request.POST['piso']
        vivienda.numero = request.POST['numero']
        vivienda.propietario = request.POST['propietario']
        vivienda.save()
        if request.POST.get('patente'):
            Vehiculo.objects.create(vivienda=vivienda, patente=request.POST['patente'].upper(), marca=request.POST.get('marca', ''), modelo=request.POST.get('modelo', ''), color=request.POST.get('color', ''))
        messages.success(request, 'La vivienda fue actualizada correctamente.')
        return redirect('inicio')
    return render(request, 'core/formulario_vivienda.html', {'titulo': 'Editar vivienda', 'vivienda': vivienda})

@administrador_requerido
def eliminar_vehiculo(request, identificador_vehiculo):
    if request.method == 'POST':
        Vehiculo.objects.filter(id=identificador_vehiculo).delete()
        messages.success(request, 'El vehículo fue eliminado correctamente.')
    return redirect('inicio')

@administrador_requerido
def eliminar_vivienda(request, identificador_vivienda):
    if request.method == 'POST':
        Vivienda.objects.filter(id=identificador_vivienda).delete()
        messages.success(request, 'La vivienda fue eliminada correctamente.')
    return redirect('inicio')
