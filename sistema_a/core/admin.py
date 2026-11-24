from django.contrib import admin
from .models import AccesoVehicular, PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cargo')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    list_filter = ('cargo',)


@admin.register(AccesoVehicular)
class AccesoVehicularAdmin(admin.ModelAdmin):
    list_display = ('patente', 'movimiento', 'fecha_hora', 'autorizado')
    search_fields = ('patente',)
    list_filter = ('movimiento', 'autorizado', 'fecha_hora')
    readonly_fields = ('fecha_hora',)
