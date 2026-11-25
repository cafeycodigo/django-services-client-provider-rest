from django.urls import path
from .views import personajes

urlpatterns = [path('characters/', personajes, name='rick-personajes')]
