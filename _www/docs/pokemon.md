---
title: "8. Integración con Pokémon"
sidebar_position: 10
---

La ruta `/api/pokemon/{nombre}/` entrega el nombre a la vista Django. La vista lo convierte a minúsculas y consulta PokéAPI. React muestra sprite, altura, peso y tipos.

```powershell
curl.exe -i http://localhost:8001/api/pokemon/pikachu/
```

Arranca `front_pokemon` con `npm install` y `npm run dev`. Busca pikachu e identifica dónde se usa `sprites.front_default` y dónde se transforma `types` en texto.

Como ampliación, elimina espacios al inicio y al final del nombre en React. En Django comprueba el estado HTTP antes de leer el JSON: el proveedor puede enviar un 404 con un cuerpo que no sea JSON. Devuelve un error controlado y prueba una búsqueda válida y una inexistente.

## Código del repositorio

```python title="sistema_b/api_pokemon/views.py"
import requests
from django.http import JsonResponse

def pokemon(request, nombre):
    respuesta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}', timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)
```

## Código del repositorio

```javascript title="front_pokemon/src/services/APIPokemon.js"
const URL_API_POKEMON = 'http://localhost:8001/api/pokemon/'

const APIPokemon = {
  async buscar(nombrePokemon) {
    const respuesta = await fetch(`${URL_API_POKEMON}${nombrePokemon}/`)

    if (!respuesta.ok) {
      throw new Error('Pokémon no encontrado')
    }

    return respuesta.json()
  },
}

export default APIPokemon
```
