from django.urls import path
from .views import proveedor

urlpatterns = [path('provider/', proveedor, name='api-test-provider')]
