from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from core.models import PerfilUsuario

from core.models import AccesoVehicular


class Command(BaseCommand):
    # Crea movimientos falsos para probar el sistema.
    help = 'Carga movimientos de acceso de ejemplo.'

    def handle(self, *args, **options):
        for nombre, clave, cargo, es_staff in [('usuario', 'usuario123', 'guardia', False), ('admin', 'admin123', 'administrador', True)]:
            usuario, creado = User.objects.get_or_create(username=nombre, defaults={'is_staff': es_staff})
            usuario.set_password(clave)
            usuario.is_staff = es_staff
            usuario.save()
            PerfilUsuario.objects.update_or_create(usuario=usuario, defaults={'cargo': cargo})
        fake = Faker('es_CL')
        plates = ['ABCD12', 'EFGH34', 'IJKL56']
        for _ in range(10):
            AccesoVehicular.objects.create(
                patente=fake.random_element(plates),
                movimiento=fake.random_element((AccesoVehicular.ENTRADA, AccesoVehicular.SALIDA)),
                autorizado=fake.boolean(chance_of_getting_true=80),
                datos_vehiculo={'source': 'seed', 'generated_by': 'Faker'},
            )
        self.stdout.write(self.style.SUCCESS('Datos aleatorios cargados en sistema A con Faker.'))
