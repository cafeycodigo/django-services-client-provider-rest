---
title: "Permitir que otros consuman mi API"
sidebar_position: 4
---

**Meta.** Entregar a otro equipo un contrato que pueda probar desde su propio cliente.

## Ejemplo de contrato

Comparte la URL base, el método, los encabezados, campos, permisos y estados. Usa datos ficticios.

| Elemento | Contrato de ejemplo |
| --- | --- |
| Base local | `http://localhost:8001` |
| Listado | `GET /api/v2/viviendas/` |
| Alta | `POST /api/v2/viviendas/` |
| Cuerpo del alta | JSON con piso entero, numero y propietario |
| Resultado | 201 con ID, 400 si la entrada es inválida |
| Autenticación | Indica el esquema que configuraste y qué cuenta puede escribir |

```powershell
curl.exe -i --json '{"piso":1,"numero":"LAB-02","propietario":"Prueba"}' http://localhost:8001/api/v2/viviendas/
```

La URL local funciona para un cliente en la misma máquina. Para un laboratorio en una red privada autorizada, ejecuta B con `manage.py runserver 0.0.0.0:8001`, configura `ALLOWED_HOSTS` con la IP o el nombre del servidor y comparte esa dirección. El servidor de desarrollo es para el laboratorio. En un despliegue usa un servidor de producción y HTTPS. GitHub Pages sirve esta documentación estática. Django requiere su propio entorno de ejecución.

Si el consumidor usa el navegador y viene de un origen distinto, registra su origen exacto en [CORS](../cors.md). La conexión de Python y curl no depende de CORS. Las cuentas y permisos se configuran en [Seguridad](./06-seguridad.md).

**Práctica guiada.** Pide a un compañero que reproduzca el GET usando tu contrato. Si recibe error de conexión, revisen URL y puerto. Si recibe 404, revisen la ruta. Si curl funciona y React falla, revisen el origen y la consola.

**Reto.** Documenta la API de calculadora con un ejemplo de éxito y otro de división por cero. El compañero debe poder reproducir las dos respuestas usando solo tu contrato.
