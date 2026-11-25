from django.db import models

# Modelos del control de acceso y perfiles de usuario.
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    CARGOS = (
        ('administrador', 'Administrador'),
        ('conserje', 'Conserje'),
        ('guardia', 'Guardia'),
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    cargo = models.CharField('cargo', max_length=30, choices=CARGOS, default='guardia')

    def __str__(self):
        return f'{self.usuario.username} - {self.get_cargo_display()}'


class AccesoVehicular(models.Model):
    ENTRADA = 'entrada'
    SALIDA = 'salida'
    MOVIMIENTOS = ((ENTRADA, 'Entrada'), (SALIDA, 'Salida'))
    patente = models.CharField('patente', max_length=12)
    movimiento = models.CharField('movimiento', max_length=7, choices=MOVIMIENTOS)
    fecha_hora = models.DateTimeField('fecha y hora', auto_now_add=True)
    autorizado = models.BooleanField('autorizado', default=False)
    datos_vehiculo = models.JSONField('datos del sistema B', default=dict, blank=True)

    class Meta:
        ordering = ('-fecha_hora',)

    def __str__(self):
        return f'{self.patente} - {self.get_movimiento_display()}'
