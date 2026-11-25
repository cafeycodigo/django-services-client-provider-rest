---
title: "Consumir una API con Python"
sidebar_position: 3
---

**Meta.** Realizar una petición, interpretar la respuesta y distinguir errores HTTP y de conexión.

## Ejemplo resuelto con requests

El ejemplo llama a la calculadora de B y se puede ejecutar desde un script Python con el entorno del proyecto. El cliente de prueba de A usa POST con `json=payload`. La consulta vehicular de A usa `urllib`. Ambos casos se explican en [comunicación A–B](../comunicacion.md) y [requests](../requests.md).

```python
import requests

try:
    respuesta = requests.get(
        "http://localhost:8001/api/calculadora/suma/",
        params={"numero_1": 10, "numero_2": 5},
        timeout=5,
    )
    respuesta.raise_for_status()
    print(respuesta.json()["resultado"])  # Esperado: 15.0
except requests.Timeout:
    print("La API tardó demasiado en responder.")
except requests.HTTPError as error:
    print(f"La API respondió HTTP {error.response.status_code}.")
except requests.RequestException:
    print("No se pudo completar la solicitud.")
```

**Práctica guiada.** Completa la misma petición para `division/` con divisor cero. Identifica qué excepción produce y por qué `raise_for_status()` va antes de leer el resultado.

**Reto.** Detén B y repite. Compara el fallo de conexión con el `400` anterior. Después consulta los ejemplos de [Rick and Morty](../rick.md) y [Pokémon](../pokemon.md) para reconocer el mismo patrón con proveedores externos.
