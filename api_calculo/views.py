import requests
from django.conf import settings
from django.http import JsonResponse

def enviar_calculo(request, operacion):
    datos = request.GET
    respuesta = requests.get(f'{settings.SYSTEM_B_CALCULADORA_URL}/{operacion}/', params={'numero_1': datos.get('numero_1'), 'numero_2': datos.get('numero_2')}, timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)
