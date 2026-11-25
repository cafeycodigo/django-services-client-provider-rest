from django.urls import path
from .views import division, multiplicacion, resta, suma, test

urlpatterns = [
    path('suma/', suma, name='calculadora-suma'),
    path('resta/', resta, name='calculadora-resta'),
    path('multiplicacion/', multiplicacion, name='calculadora-multiplicacion'),
    path('division/', division, name='calculadora-division'),
    path('test/', test, name='calculadora-test'),
]
