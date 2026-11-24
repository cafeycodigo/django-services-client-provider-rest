from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AccesoVehicular

@login_required
def inicio(request):
    return render(request, 'core/inicio.html', {'accesos': AccesoVehicular.objects.all()[:20]})
