from django.db import models

# Modelos del registro de viviendas y vehículos del condominio.
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


class Vivienda(models.Model):
    piso = models.PositiveIntegerField('piso')
    numero = models.CharField('número', max_length=20)
    propietario = models.CharField('propietario', max_length=150)

    class Meta:
        ordering = ('piso', 'numero')
        constraints = [
            models.UniqueConstraint(fields=('piso', 'numero'), name='unique_vivienda_piso_numero')
        ]

    def __str__(self):
        return f'Piso {self.piso} - Casa {self.numero}'


class Vehiculo(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='vehiculos')
    patente = models.CharField('patente', max_length=12, unique=True)
    marca = models.CharField('marca', max_length=80, blank=True)
    modelo = models.CharField('modelo', max_length=80, blank=True)
    color = models.CharField('color', max_length=40, blank=True)
    activo = models.BooleanField('activo', default=True)

    class Meta:
        ordering = ('patente',)

    def __str__(self):
        return self.patente
