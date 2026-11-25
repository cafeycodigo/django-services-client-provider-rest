---
title: "7. Integración con Rick and Morty"
sidebar_position: 9
---

La vista Django actúa como intermediaria. React consume `GET /api/rick/characters/` de B y Django consulta el proveedor externo con `requests`.

1. Levanta B y verifica que la respuesta local contenga `results`.
2. Entra en `front_rick`, ejecuta `npm install` y luego `npm run dev`.
3. Sigue `APIRick.personajes()` desde el efecto de carga hasta el renderizado de cada tarjeta.
4. Identifica los campos `name`, `image`, `status` y `species` en la respuesta y su uso en React.

Para desarrollar paginación, recibe un número de página positivo en Django, pásalo al proveedor con `params` y usa los botones de React para cambiar de página. Agrega un mensaje de error cuando la API externa no responda.

## Código del repositorio

```python title="sistema_b/api_rick/views.py"
import requests
from django.http import JsonResponse

def personajes(request):
    respuesta = requests.get('https://rickandmortyapi.com/api/character', timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)
```

## Código del repositorio

```javascript title="front_rick/src/services/APIRick.js"
const URL_API_RICK = 'http://localhost:8001/api/rick/characters/'

const APIRick = {
  async personajes() {
    const respuesta = await fetch(URL_API_RICK)

    if (!respuesta.ok) {
      throw new Error('No se pudieron cargar los personajes')
    }

    return respuesta.json()
  },
}

export default APIRick
```
