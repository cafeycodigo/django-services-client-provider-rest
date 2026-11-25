---
title: "11. Servicios separados en React"
sidebar_position: 13
---

El servicio concentra las rutas, los métodos y la conversión JSON. El componente conserva el estado del formulario, decide qué método invocar y actualiza lo que ve el usuario.

En el servicio de viviendas, `crear` y `actualizar` comparten la función `enviar`. `eliminar` solo valida el estado HTTP. Conserva las llamadas como `APIServiceVivienda.crear(datos)` porque los métodos del objeto usan `this.enviar`.

Como práctica, cambia la base del servicio a `import.meta.env.VITE_API_URL` con el valor local como respaldo. Luego configura un puerto diferente mediante `.env.local` y confirma el destino en Red.

## Código del repositorio

```javascript title="frontend_b/src/services/APIServiceVivienda.js"
const URL_BASE = 'http://localhost:8001/api/v2/viviendas/'

// Servicio responsable de comunicarse con la API de viviendas.
const APIServiceVivienda = {
  async listar() {
    const respuesta = await fetch(URL_BASE)
    if (!respuesta.ok) throw new Error('No fue posible cargar las viviendas')
    return respuesta.json()
  },

  async crear(datosVivienda) {
    return this.enviar(URL_BASE, 'POST', datosVivienda)
  },

  async actualizar(idVivienda, datosVivienda) {
    return this.enviar(`${URL_BASE}${idVivienda}/`, 'PUT', datosVivienda)
  },

  async eliminar(idVivienda) {
    const respuesta = await fetch(`${URL_BASE}${idVivienda}/`, { method: 'DELETE' })
    if (!respuesta.ok) throw new Error('No fue posible eliminar la vivienda')
  },

  async enviar(url, metodo, datos) {
    const respuesta = await fetch(url, {
      method: metodo,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos),
    })
    if (!respuesta.ok) throw new Error('La API rechazó la operación')
    return respuesta.json()
  },
}

export default APIServiceVivienda
```
