import requests
from django.conf import settings
from django.http import JsonResponse

def enviar_a_calculadora(request, operacion):
    numero_1 = request.GET.get('numero_1')
    numero_2 = request.GET.get('numero_2')
    respuesta = requests.get(f'{settings.SYSTEM_B_CALCULADORA_URL}/{operacion}/', params={'numero_1': numero_1, 'numero_2': numero_2}, timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)

def suma(request):
    return enviar_a_calculadora(request, 'suma')

def resta(request):
    return enviar_a_calculadora(request, 'resta')

def multiplicacion(request):
    return enviar_a_calculadora(request, 'multiplicacion')

def division(request):
    return enviar_a_calculadora(request, 'division')

def test(request):
    return enviar_a_calculadora(request, 'test')
