---
title: "12. CRUD desde React"
sidebar_position: 14
---

## Recorrido de una edición

1. Carga las viviendas con GET. Selecciona una fila y copia sus campos editables al formulario.
2. Conserva el ID seleccionado para decidir entre POST de colección y PUT de detalle.
3. Al guardar, espera la respuesta. Recarga el listado si la escritura fue exitosa.
4. Al eliminar, confirma el registro seleccionado, envía DELETE y recarga la tabla.

```json
{
  "piso": 1,
  "numero": "LAB-01",
  "propietario": "Persona de prueba"
}
```

Crea una vivienda ficticia con ese cuerpo. Espera 201, copia el ID de la respuesta y edita el propietario con PUT. Prueba reutilizar piso y número para observar la validación de unicidad. Finalmente elimina solo el registro de prueba y verifica 204 seguido de 404 al consultar su detalle.

Como ampliación, muestra los mensajes de validación junto a cada campo y bloquea el botón mientras se envía una solicitud para reducir escrituras duplicadas.

## Implementar el guardado en el componente

En `frontend_b/src/App.jsx`, revisa el envío del formulario. Este fragmento didáctico se puede adaptar al componente. Recibe como argumentos el ID y los datos del formulario para mostrar explícitamente qué determina el método HTTP.

```javascript
async function guardarVivienda(id, formulario) {
  const datos = {
    piso: Number(formulario.piso),
    numero: formulario.numero.trim(),
    propietario: formulario.propietario.trim(),
  }

  // El ID distingue un registro nuevo de uno seleccionado para edición.
  if (id == null) {
    await APIServiceVivienda.crear(datos)
  } else {
    await APIServiceVivienda.actualizar(id, datos)
  }

  // Recarga únicamente después de que la API confirme el cambio.
  return APIServiceVivienda.listar()
}
```

En el manejador de envío, llama a `evento.preventDefault()` y actualiza el estado con la lista devuelta. Coloca esa llamada dentro de un `try/catch` para conservar el contenido del formulario si la API rechaza los datos. Comprueba que una edición envíe el ID en la URL y que el registro aparezca actualizado al recargar el navegador.
