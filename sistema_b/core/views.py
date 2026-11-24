from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Vehiculo, Vivienda

@login_required
def inicio(request):
    return render(request, 'core/inicio.html', {'viviendas': Vivienda.objects.prefetch_related('vehiculos'), 'vehiculos': Vehiculo.objects.select_related('vivienda')})
