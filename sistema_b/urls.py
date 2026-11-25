"""
URL configuration for sistema_b project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from core.views import cerrar_sesion, crear_vehiculo, crear_vivienda, dashboard_comunidad, detalle_vivienda, editar_vivienda, eliminar_vehiculo, eliminar_vivienda, iniciar_sesion, inicio, lista_vehiculos

urlpatterns = [
    # Página principal y autenticación.
    path('', RedirectView.as_view(url='/comunidad/', permanent=False), name='inicio'),
    path('comunidad/', dashboard_comunidad, name='comunidad'),
    path('comunidad/home/', inicio, name='comunidad-home'),
    path('comunidad/viviendas/', inicio, name='comunidad-viviendas'),
    path('comunidad/vehiculos/', lista_vehiculos, name='comunidad-vehiculos'),
    path('comunidad/vehiculo/', lista_vehiculos, name='comunidad-vehiculo'),
    path('comunidad/viviendas/nueva/', crear_vivienda, name='crear-vivienda'),
    path('comunidad/viviendas/<int:identificador_vivienda>/', detalle_vivienda, name='detalle-vivienda'),
    path('comunidad/viviendas/<int:identificador_vivienda>/vehiculos/nuevo/', crear_vehiculo, name='crear-vehiculo'),
    path('comunidad/viviendas/<int:identificador_vivienda>/editar/', editar_vivienda, name='editar-vivienda'),
    path('comunidad/viviendas/<int:identificador_vivienda>/eliminar/', eliminar_vivienda, name='eliminar-vivienda'),
    path('comunidad/vehiculos/<int:identificador_vehiculo>/eliminar/', eliminar_vehiculo, name='eliminar-vehiculo'),
    path('comunidad/login/', iniciar_sesion, name='login'),
    path('comunidad/logout/', cerrar_sesion, name='logout'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_v1.urls')),
    path('api/test/', include('api_test.urls')),
    path('api/calculadora/', include('api_calculadora.urls')),
    path('api/calculo/', include('api_calculo.urls')),
    path('api/v2/', include('api_v2.urls')),
]
