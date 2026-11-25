---
title: "Qué es una API REST"
sidebar_position: 1
---

**Meta.** Identificar el recurso, el método, la URL y el estado HTTP de una operación.

## Ejemplo resuelto

En el Sistema B, una vivienda es un **recurso**. La URL de colección es `/api/v2/viviendas/` y la de un elemento concreto agrega su ID. El método expresa la operación. JSON es una representación de los datos. REST es un estilo de arquitectura que organiza la interacción alrededor de recursos y una interfaz uniforme. En HTTP, cada petición aporta el contexto necesario para procesarla.

```powershell
curl.exe -i -H "Accept: application/json" http://localhost:8001/api/v2/viviendas/
```

La primera línea de la respuesta indica el estado. `Content-Type` indica el formato del cuerpo. Si todavía no hay registros, una lista vacía sigue siendo un éxito `200`.

| Petición | Qué hace | Éxito esperado |
| --- | --- | --- |
| GET colección o detalle | Leer | 200 |
| POST colección | Crear | 201 |
| PUT detalle | Enviar la representación editable completa | 200 |
| PATCH detalle | Cambiar campos específicos | 200 |
| DELETE detalle | Eliminar | 204 sin cuerpo |

**Práctica guiada.** Obtén un ID real de la lista y agrégalo al final de la URL. Predice la diferencia entre recibir un arreglo y recibir un objeto.

**Reto.** Consulta un ID que no exista. Registra el estado y explica por qué es distinto de una colección vacía. La respuesta esperada es `404`.
