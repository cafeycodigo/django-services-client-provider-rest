---
title: "1. Sistema A · Control de accesos"
sidebar_position: 2
---

## Del modelo a la pantalla

A guarda una fila por solicitud válida, con patente, movimiento, hora, decisión y la respuesta recibida de B. Guardar una copia de la respuesta permite revisar lo que B informó en ese momento aunque el padrón cambie después. El panel web muestra los 20 movimientos recientes.

1. Inspecciona el modelo y localiza sus opciones de movimiento.
2. Abre `sistema_a/core/views.py` y sigue `iniciar_sesion`: Django verifica las credenciales con `authenticate` y guarda la sesión con `login`.
3. En `sistema_a/sistema_a/urls.py`, sigue la ruta raíz hacia `inicio` y luego al template `core/inicio.html`.
4. Abre la API de accesos en el capítulo de comunicación para seguir la escritura de la fila.

## Práctica

En una copia de laboratorio agrega un filtro de patente al panel. Lee `request.GET.get('patente', '').strip()` y aplica `filter(patente__iexact=patente)` antes de limitar el queryset a 20 filas. Verifica la lista con y sin el filtro. Conserva la protección de sesión de la vista. La eliminación web está reservada a staff o superusuario.

## Código del repositorio

```python title="sistema_a/core/models.py"
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
```
