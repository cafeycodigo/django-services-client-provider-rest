from rest_framework.routers import DefaultRouter

from .views import VehiculoViewSet, ViviendaViewSet

router = DefaultRouter()
router.register('viviendas', ViviendaViewSet, basename='api-v2-vivienda')
router.register('vehiculos', VehiculoViewSet, basename='api-v2-vehiculo')

urlpatterns = router.urls
