from django.urls import path
from .views import division, multiplicacion, resta, suma, test

urlpatterns = [
    path('suma/', suma, name='calculo-suma'),
    path('resta/', resta, name='calculo-resta'),
    path('multiplicacion/', multiplicacion, name='calculo-multiplicacion'),
    path('division/', division, name='calculo-division'),
    path('test/', test, name='calculo-test'),
]
