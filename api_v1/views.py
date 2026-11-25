from django.http import JsonResponse
from django.views.decorators.http import require_GET

from core.models import Vehiculo


@require_GET
def vehicle_lookup(request, plate):
    vehiculo = Vehiculo.objects.select_related('vivienda').filter(
        patente__iexact=plate.strip(), activo=True
    ).first()
    if vehiculo is None:
        return JsonResponse({'authorized': False, 'detail': 'Vehículo no registrado'}, status=404)
    return JsonResponse({
        'authorized': True,
        'plate': vehiculo.patente,
        'house': {
            'floor': vehiculo.vivienda.piso,
            'number': vehiculo.vivienda.numero,
            'owner': vehiculo.vivienda.propietario,
        },
        'vehicle': {
            'brand': vehiculo.marca,
            'model': vehiculo.modelo,
            'color': vehiculo.color,
        },
    })
