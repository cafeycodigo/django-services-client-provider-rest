---
title: "Proteger la API con credenciales o token"
sidebar_position: 6
---

**Meta.** Proteger una ruta de DRF y demostrar la diferencia entre autenticación y autorización.

El login web de Django identifica una sesión. Cada API también necesita definir quién puede leer o modificar sus datos. Este laboratorio propone proteger **ViviendaViewSet** en B. El cambio se aplica a ese recurso. Revisa por separado VehiculoViewSet y API v1 si necesitas proteger todo el padrón.

## Paso 1. Crear una cuenta de prueba

Desde la raíz crea una cuenta staff de laboratorio con `createsuperuser` en B. Para verificar la autorización, crea también una cuenta activa sin `is_staff` desde Django Admin.

```powershell
& .\venv\Scripts\python.exe sistema_b/manage.py createsuperuser
```

## Paso 2. Usuario y contraseña con Basic Auth

Añade los imports y las dos propiedades al ViewSet existente en `sistema_b/api_v2/views.py`. Conserva su queryset y serializer. Basic envía credenciales en cada petición, codificadas en Base64. Usa HTTPS fuera del laboratorio local.

```python
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

# Dentro de ViviendaViewSet
authentication_classes = [BasicAuthentication]
permission_classes = [IsAdminUser]
```

```powershell
curl.exe -i -u usuario_de_prueba http://localhost:8001/api/v2/viviendas/
```

Curl solicita la contraseña. Sin credenciales espera `401`. Con usuario válido sin staff espera `403`. Con staff espera `200` para el GET. `IsAdminUser` comprueba `is_staff`. Si el ejercicio requiere acceso para cualquier cuenta autenticada, usa `IsAuthenticated` con esa intención explícita.

## Paso 3. Token de DRF

Agrega `rest_framework.authtoken` a `INSTALLED_APPS` del Sistema B y aplica las migraciones. Genera un token para la cuenta de laboratorio.

```powershell
& .\venv\Scripts\python.exe sistema_b/manage.py migrate
& .\venv\Scripts\python.exe sistema_b/manage.py drf_create_token usuario_de_prueba
```

Reemplaza `BasicAuthentication` por `TokenAuthentication` de `rest_framework.authentication`. Conserva `IsAdminUser`. Ese token se envía con el prefijo `Token`. El esquema de este ejemplo es el token integrado de DRF.

```http
GET /api/v2/viviendas/
Authorization: Token TOKEN_DE_PRUEBA
Accept: application/json
```

Prueba el encabezado en tu cliente HTTP. Mantén el token fuera de commits, capturas, logs y variables `VITE_*`. Los valores incluidos por Vite quedan al alcance del navegador. Revoca el token de laboratorio desde Django Admin al terminar. Usa HTTPS para protegerlo durante el transporte.

## Paso 4. Enviar el token desde React

Para este ejemplo el token se recibe en memoria durante la sesión de prueba. Adapta el servicio de viviendas para aceptar credenciales por solicitud. La autorización sigue estando en Django.

```javascript
async function listarViviendas(token) {
  const respuesta = await fetch('http://localhost:8001/api/v2/viviendas/', {
    headers: { Authorization: `Token ${token}` },
  })
  if (!respuesta.ok) throw new Error(`HTTP ${respuesta.status}`)
  return respuesta.json()
}
```

Si en otra implementación usas sesiones por cookie, las peticiones de escritura exigen configurar también CSRF. Con `Authorization` entre orígenes revisa el preflight de CORS. CORS y los botones visibles en React no conceden permisos de API.

**Práctica guiada.** Prueba sin token, con un token de usuario sin staff y con el token de staff. Anota `401 → 403 → 200`.

**Reto.** Protege también VehiculoViewSet y agrega pruebas para una escritura autorizada y otra denegada. Explica por qué un token válido puede recibir `403`. [Autenticación en DRF](https://www.django-rest-framework.org/api-guide/authentication/) · [Permisos en DRF](https://www.django-rest-framework.org/api-guide/permissions/)
