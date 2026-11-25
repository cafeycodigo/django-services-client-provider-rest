import requests
from django.http import JsonResponse

def personajes(request):
    respuesta = requests.get('https://rickandmortyapi.com/api/character', timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)
