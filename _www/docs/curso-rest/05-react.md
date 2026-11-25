---
title: "Consumir una API desde React"
sidebar_position: 5
---

**Meta.** Conectar la pantalla a un servicio y mostrar estados de carga, éxito y error.

## Ejemplo resuelto de lectura

El proyecto ya concentra las llamadas HTTP en `frontend_b/src/services/APIServiceVivienda.js`. Este ejemplo reducido muestra cómo usar ese servicio desde un componente. Para conectarlo, usa un archivo junto a `App.jsx` e importa el componente desde allí.

```jsx
import { useEffect, useState } from 'react'
import APIServiceVivienda from './services/APIServiceVivienda'

export default function ListaViviendas() {
  const [viviendas, setViviendas] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    let activo = true

    APIServiceVivienda.listar()
      .then(datos => { if (activo) setViviendas(datos) })
      .catch(fallo => { if (activo) setError(fallo.message) })
      .finally(() => { if (activo) setCargando(false) })

    return () => { activo = false }
  }, [])

  if (cargando) return <p role="status">Cargando viviendas…</p>
  if (error) return <p role="alert">{error}</p>
  if (viviendas.length === 0) return <p>No hay viviendas registradas.</p>

  return (
    <ul>
      {viviendas.map(vivienda => <li key={vivienda.id}>{vivienda.numero}</li>)}
    </ul>
  )
}
```

Arranca B y luego `npm run dev` en `frontend_b`. Abre Red en DevTools e identifica el GET. El servicio verifica `respuesta.ok` y convierte el JSON. El componente administra lo que se ve.

**Práctica guiada.** Apaga B y recarga. Recupera la conexión y verifica la carga exitosa.

**Reto.** Agrega un formulario que llame a `APIServiceVivienda.crear(datos)`. Recarga el listado tras el `201`. Usa el [CRUD existente](../crud.md) para comparar tu flujo. Un DELETE `204` se procesa sin leer JSON.
