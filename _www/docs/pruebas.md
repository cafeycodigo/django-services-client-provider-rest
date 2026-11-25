---
title: "14. Pruebas, mejoras y entrega"
sidebar_position: 16
---

## Revisar por capas

```powershell
& .\venv\Scripts\python.exe sistema_a/manage.py check
& .\venv\Scripts\python.exe sistema_b/manage.py check
# Desde el frontend que quieras comprobar, con dependencias instaladas
npm run build
```

| Caso | Resultado esperado |
| --- | --- |
| Patente activa en B | 200 y authorized verdadero |
| Patente inexistente en B | 404 |
| Entrada autorizada en A | 201 y fila persistida |
| División por cero | 400 |
| Alta de vivienda en v2 | 201 y un identificador |
| Borrado de vivienda de prueba | 204 y posterior 404 |

## Entrega del estudiante

Implementa una mejora de contrato y una de interfaz. Por ejemplo, distingue en A la patente desconocida de un fallo remoto y muestra ambos resultados en React. Entrega el diff, un ejemplo de petición y respuesta por caso, y evidencia de la fila persistida. Para automatizar una llamada externa usa un mock que reproduzca éxito, 404 y timeout. Ejecuta los casos sin depender de Internet.

Antes de un despliegue revisa permisos de API v2, CORS y CSRF por proceso, credenciales iniciales, URLs configurables y errores externos. Trabaja con datos ficticios durante la práctica.

Consulta las [propuestas de desarrollo](./propuestas.md) para elegir un trabajo con pasos de implementación y criterios de aceptación.
