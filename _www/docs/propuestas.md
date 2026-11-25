---
title: "15. Propuestas de desarrollo"
sidebar_position: 17
---

Estas propuestas son trabajos de ampliación del laboratorio. Elige una como proyecto y usa sus criterios de aceptación para demostrar el resultado.

## 1. Explicar por qué se rechazó un acceso

**Objetivo.** Distinguir en el Sistema A una patente que B no reconoce de una falla de comunicación.

1. Revisa `sistema_a/api_v1/views.py` y localiza la consulta con `urlopen`.
2. Captura `HTTPError` antes de `URLError`. Trata el 404 de B como patente no registrada y una falla de red como proveedor no disponible.
3. Guarda la causa junto al movimiento y devuelve un código estable en el JSON. Muestra un texto correspondiente en `frontend_a/src/App.jsx`.

```python
# Fragmento propuesto dentro del manejo de errores de la consulta a B.
except HTTPError as error:
    causa = "patente_no_registrada" if error.code == 404 else "error_del_proveedor"
except (URLError, TimeoutError):
    causa = "proveedor_no_disponible"
```

**Aceptación.** Una patente activa conserva el flujo exitoso. Una patente desconocida y B desconectado producen causas distintas. Verifica cada caso con un mock y comprueba el movimiento almacenado.

## 2. Registrar vehículos desde React

**Objetivo.** Ampliar el CRUD de viviendas para registrar un vehículo en una vivienda existente a través de API v2.

1. En `sistema_b/api_v2/serializers.py`, expón el campo `vivienda` del modelo `Vehiculo`.
2. En `frontend_b/src/services/`, crea un servicio para POST a `/api/v2/vehiculos/`.
3. En React, ofrece un selector con las viviendas reales y envía su ID. Muestra los errores de validación cerca de los campos.
4. Aplica permisos explícitos al ViewSet y prueba las escrituras con un administrador de laboratorio.

```json
{
  "vivienda": 1,
  "patente": "LABA12",
  "marca": "Ejemplo",
  "activo": true
}
```

**Aceptación.** Con un ID real y una patente nueva, POST devuelve 201 y el vehículo aparece en el detalle de la vivienda. Una vivienda inexistente o una patente duplicada devuelve 400. Una cuenta sin permiso no puede crear vehículos.

## 3. Llevar la calculadora a dos procesos

**Objetivo.** Conectar React → Sistema A → Sistema B y verificar cada tramo por separado.

1. Crea `api_calculo` en A siguiendo las vistas y las rutas explícitas de B.
2. Configura la URL del proveedor de B en los settings de A.
3. En `front_calculadora/src/services/APIServiceCalculadora.js`, cambia el destino hacia A y configura CORS para ese origen.
4. Usa `requests` con timeout en A. Conserva el 400 del proveedor para errores como división por cero y devuelve 502 si el proveedor no está disponible.

```text
React → GET localhost:8000/api/calculo/suma/?numero_1=10&numero_2=5
A     → GET localhost:8001/api/calculadora/suma/?numero_1=10&numero_2=5
B     → {"operacion":"suma","resultado":15.0}
```

**Aceptación.** Las cuatro operaciones funcionan desde React. DevTools muestra una solicitud a A, el registro de B muestra la consulta entrante y la interfaz informa el fallo cuando B está apagado.

## 4. Mejorar las integraciones externas

**Objetivo.** Agregar paginación a Rick and Morty y mensajes de error específicos al buscador Pokémon.

1. En `api_rick/views.py`, valida un parámetro `page` entero positivo y reenvíalo con `requests.get(..., params={"page": pagina}, timeout=5)`.
2. En `front_rick`, guarda la página en el estado y actualiza el listado al cambiarla. Usa los metadatos de la respuesta para habilitar los botones.
3. En `api_pokemon/views.py`, revisa el estado HTTP antes de convertir el cuerpo con `json()`. Devuelve un error JSON propio si el proveedor responde 404.
4. En `front_pokemon`, presenta estados distintos para búsqueda en curso, Pokémon inexistente y falla de conexión.

**Aceptación.** La página 2 cambia la lista de personajes. Un Pokémon válido muestra sus datos. Un nombre inexistente muestra un aviso. Simula esas respuestas para que las pruebas sean repetibles.

## Qué entregar

- El cambio de código con los archivos identificados.
- Comandos para reproducirlo y, si aplica, el JSON de entrada.
- Una prueba de éxito y una de error por comportamiento nuevo.
- Una explicación breve del recorrido de la solicitud y del resultado observado.
