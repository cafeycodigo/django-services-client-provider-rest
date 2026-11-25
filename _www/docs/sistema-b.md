---
title: "1. Sistema B · Registro del condominio"
sidebar_position: 3
---

## Modelo y operación administrativa

Cada vivienda se identifica por la combinación de piso y número. Cada vehículo tiene patente única y pertenece a una vivienda. `related_name='vehiculos'` habilita `vivienda.vehiculos.all()`, y `CASCADE` elimina vehículos asociados cuando se elimina su vivienda.

1. Inicia sesión en `/comunidad/login/` con un administrador de prueba.
2. Abre `/comunidad/viviendas/` y crea una vivienda ficticia. Anota piso y número.
3. Abre el detalle y añade un vehículo. Verifica su patente en `/comunidad/vehiculos/`.
4. Consulta esa misma patente en API v1. La API v2 permite ver la vivienda con sus vehículos anidados.

Las vistas de escritura web comprueban staff, superusuario o cargo administrador. El login en modo administrador comprueba staff o superusuario. Revisa ambos puntos al preparar cuentas.

## Práctica

Desde Django Admin desactiva el vehículo y consulta nuevamente API v1. Debe responder 404 aunque el registro siga en el padrón. Propón qué campo mostrar en el listado para distinguir activos e inactivos.

## Código del repositorio

```python title="sistema_b/core/models.py"
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
```
