import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def cliente(request):
    try:
        datos = json.loads(request.body or '{}')
        payload = {'valor_1': datos['valor_1'], 'valor_2': datos['valor_2'], 'operacion': datos.get('operacion', 'suma')}
        respuesta = requests.post(settings.SYSTEM_B_TEST_API_URL, json=payload, timeout=5)
        respuesta.raise_for_status()
        resultado = respuesta.json()
        return JsonResponse({'cliente': 'sistema_a', 'proveedor': 'sistema_b', 'resultado': resultado})
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        return JsonResponse({'error': str(error)}, status=400)
    except requests.RequestException as error:
        return JsonResponse({'error': f'No fue posible contactar al proveedor: {error}'}, status=502)
