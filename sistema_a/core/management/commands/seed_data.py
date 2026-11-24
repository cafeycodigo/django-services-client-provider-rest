from django.core.management.base import BaseCommand
from faker import Faker

from core.models import AccesoVehicular


class Command(BaseCommand):
    help = 'Carga movimientos de acceso de ejemplo.'

    def handle(self, *args, **options):
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
