from django.contrib import admin
from .models import PerfilUsuario, Vehiculo, Vivienda


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cargo')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    list_filter = ('cargo',)


@admin.register(Vivienda)
class ViviendaAdmin(admin.ModelAdmin):
    list_display = ('piso', 'numero', 'propietario', 'cantidad_vehiculos')
    search_fields = ('numero', 'propietario')
    list_filter = ('piso',)

    @admin.display(description='vehículos')
    def cantidad_vehiculos(self, obj):
        return obj.vehiculos.count()


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'vivienda', 'marca', 'modelo', 'color', 'activo')
    search_fields = ('patente', 'marca', 'modelo', 'vivienda__numero', 'vivienda__propietario')
    list_filter = ('activo', 'marca', 'color')
