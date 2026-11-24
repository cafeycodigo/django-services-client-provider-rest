from django.urls import path

from .views import register_access

urlpatterns = [
    path('access/', register_access, name='register-access'),
]
