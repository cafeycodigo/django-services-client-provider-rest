from django.urls import path

from .views import vehicle_lookup

urlpatterns = [
    path('vehicles/<str:plate>/', vehicle_lookup, name='vehicle-lookup'),
]
