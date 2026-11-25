---
title: "10. Consumo mediante fetch"
sidebar_position: 12
---

Una respuesta HTTP 404 o 500 todavía produce un objeto Response. Revisa `respuesta.ok` antes de actualizar el estado. Una falla de red puede rechazar la promesa directamente.

```javascript
// Ejemplo para el frontend de viviendas
async function listarViviendas() {
  const respuesta = await fetch('http://localhost:8001/api/v2/viviendas/')
  if (!respuesta.ok) {
    throw new Error(`La API respondió HTTP ${respuesta.status}`)
  }
  return respuesta.json()
}
```

1. Llama a la función al cargar el componente y guarda el resultado en el estado.
2. Muestra un mensaje de error si se rechaza la promesa.
3. Apaga B y comprueba que la interfaz pueda mostrar el fallo sin perder el control.
4. En un DELETE exitoso con 204, termina sin llamar a `json()`.
