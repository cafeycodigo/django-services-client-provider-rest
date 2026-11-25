---
title: "4. Configuración de CORS"
sidebar_position: 6
---

El origen incluye protocolo, host y puerto. Vite en `localhost:5173` y B en `localhost:8001` son orígenes distintos. El backend puede responder correctamente a curl y el navegador puede bloquear la lectura por CORS.

## Configuración en B

El proyecto registra `corsheaders`, coloca su middleware antes de `CommonMiddleware` y permite todos los orígenes. Este fragmento es una propuesta de configuración local restringida. Sustituye el origen por el puerto que Vite muestre.

```python
# Añade corsheaders a la lista existente de INSTALLED_APPS.
# Inserta CorsMiddleware antes de CommonMiddleware.
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]
```

En DevTools → Red, guarda una vivienda con React y examina OPTIONS y POST. Comprueba `Origin` y `Access-Control-Allow-Origin`. Si el POST devuelve 403, revisa permisos o CSRF. CORS controla el acceso desde el navegador y CSRF protege solicitudes basadas en sesión. Para el frontend de A revisa la configuración de A por separado.
