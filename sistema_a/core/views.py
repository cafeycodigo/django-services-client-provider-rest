from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from .models import AccesoVehicular

def es_administrador(usuario):
    return usuario.is_staff or usuario.is_superuser

administrador_requerido = user_passes_test(es_administrador, login_url='/login/')

def iniciar_sesion(request):
    error = None
    if request.method == 'POST':
        usuario = authenticate(request, username=request.POST.get('usuario'), password=request.POST.get('contrasena'))
        tipo = request.POST.get('tipo_usuario', 'usuario')
        es_admin = usuario is not None and (usuario.is_staff or usuario.is_superuser)
        es_usuario = usuario is not None and hasattr(usuario, 'perfil') and usuario.perfil.cargo != 'administrador'
        if usuario is not None and ((tipo == 'administrador' and es_admin) or (tipo == 'usuario' and es_usuario)):
            login(request, usuario)
            return redirect('inicio')
        error = 'Credenciales incorrectas o tipo de acceso no autorizado.'
    return render(request, 'registration/login.html', {'error': error})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def inicio(request):
    return render(request, 'core/inicio.html', {'accesos': AccesoVehicular.objects.all()[:20]})

@administrador_requerido
def eliminar_acceso(request, identificador_acceso):
    if request.method == 'POST':
        AccesoVehicular.objects.filter(id=identificador_acceso).delete()
        messages.success(request, 'El acceso fue eliminado correctamente.')
    return redirect('inicio')
