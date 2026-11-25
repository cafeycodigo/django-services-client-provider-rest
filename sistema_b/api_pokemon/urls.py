from django.urls import path
from .views import pokemon

urlpatterns = [path('<str:nombre>/', pokemon, name='pokemon-detalle')]
