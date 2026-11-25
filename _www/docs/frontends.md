---
title: "9. Frontends React"
sidebar_position: 11
---

| Carpeta | Servicio | Destino |
| --- | --- | --- |
| frontend_a | APIServiceAcceso | A · accesos |
| frontend_b | APIServiceVivienda | B · API v2 |
| front_calculadora | APIServiceCalculadora | B · proveedor de la calculadora |
| front_rick | APIRick | B · personajes |
| front_pokemon | APIPokemon | B · búsqueda por nombre |

```powershell
cd frontend_b
npm install
npm run dev
```

Abre la URL impresa por Vite. Sigue `index.html → main.jsx → App.jsx → src/services`. Vite transforma JSX, React administra el estado y el servicio realiza la solicitud HTTP.

## Práctica

Abre la pestaña Red y ejecuta una suma en `front_calculadora`. Verifica el destino y los parámetros. Para `frontend_a`, compara el valor inicial del selector con `entrada` y `salida`, que son los valores aceptados por A. Antes de probar escrituras desde ese frontend, verifica CORS y CSRF en A.

## Código del repositorio

```javascript title="front_calculadora/src/services/APIServiceCalculadora.js"
const URL_API = 'http://localhost:8001/api/calculadora'

// Servicio que conecta React con las operaciones del Sistema B.
const APIServiceCalculadora = {
  async calcular(operacion, numero1, numero2) {
    const parametros = new URLSearchParams({ numero_1: numero1, numero_2: numero2 })
    const respuesta = await fetch(`${URL_API}/${operacion}/?${parametros}`)
    const datos = await respuesta.json()
    if (!respuesta.ok) throw new Error(datos.error || 'La API devolvió un error')
    return datos
  },
}

export default APIServiceCalculadora
```
