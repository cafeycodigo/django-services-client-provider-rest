from django.urls import path
from .views import calcular
urlpatterns = [path('<str:operacion>/', calcular)]
