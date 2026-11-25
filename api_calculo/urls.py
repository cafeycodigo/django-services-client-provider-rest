from django.urls import path
from .views import enviar_calculo
urlpatterns = [path('<str:operacion>/', enviar_calculo)]
