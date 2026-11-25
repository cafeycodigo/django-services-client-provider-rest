from django.urls import path
from .views import cliente

urlpatterns = [path('client/', cliente, name='api-test-client')]
