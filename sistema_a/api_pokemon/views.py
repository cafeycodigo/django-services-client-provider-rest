import requests
from django.http import JsonResponse

def pokemon(request, nombre):
    respuesta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}', timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)
