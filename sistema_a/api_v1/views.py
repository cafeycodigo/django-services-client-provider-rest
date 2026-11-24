import json
from urllib.error import URLError
from urllib.request import urlopen

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from core.models import AccesoVehicular


@require_POST
def register_access(request):
    try:
        payload = json.loads(request.body or '{}')
        plate = str(payload['plate']).strip().upper()
        movement = payload.get('movement', AccesoVehicular.ENTRADA)
        if movement not in dict(AccesoVehicular.MOVIMIENTOS):
            raise ValueError('movement debe ser entrada o salida')
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return JsonResponse({'detail': str(exc)}, status=400)

    url = f"{settings.SYSTEM_B_API_URL}/{plate}/"
    try:
        with urlopen(url, timeout=3) as response:
            data = json.loads(response.read().decode('utf-8'))
        authorized = bool(data.get('authorized'))
    except (URLError, TimeoutError, ValueError):
        data = {'authorized': False, 'detail': 'No fue posible consultar el sistema B'}
        authorized = False

    access = AccesoVehicular.objects.create(patente=plate, movimiento=movement, autorizado=authorized, datos_vehiculo=data)
    return JsonResponse({'id': access.id, 'plate': access.patente, 'movement': access.movimiento, 'authorized': access.autorizado, 'vehicle': data}, status=201 if authorized else 403)
