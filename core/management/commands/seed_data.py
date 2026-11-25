from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from core.models import PerfilUsuario

from core.models import Vehiculo, Vivienda


class Command(BaseCommand):
    # Crea viviendas y vehículos falsos para probar el sistema.
    help = 'Carga casas y vehículos de ejemplo del condominio.'

    def handle(self, *args, **options):
        for nombre, clave, cargo, es_staff in [('usuario', 'usuario123', 'guardia', False), ('admin', 'admin123', 'administrador', True)]:
            usuario, creado = User.objects.get_or_create(username=nombre, defaults={'is_staff': es_staff})
            usuario.set_password(clave)
            usuario.is_staff = es_staff
            usuario.save()
            PerfilUsuario.objects.update_or_create(usuario=usuario, defaults={'cargo': cargo})
        fake = Faker('es_CL')
        used_plates = set(Vehiculo.objects.values_list('patente', flat=True))
        for index in range(1, 6):
            piso = ((index - 1) // 3) + 1
            numero = str(100 + index)
            propietario = fake.name()
            patente = fake.bothify(text='????##').upper()
            while patente in used_plates:
                patente = fake.bothify(text='????##').upper()
            used_plates.add(patente)
            datos_vehiculo = {
                'patente': patente,
                'marca': fake.random_element(('Toyota', 'Kia', 'Suzuki', 'Hyundai', 'Mazda')),
                'modelo': fake.word().title(),
                'color': fake.color_name(),
            }
            
            house, _ = Vivienda.objects.update_or_create(
                piso=piso, numero=numero, defaults={'propietario': propietario}
            )
            Vehiculo.objects.update_or_create(
                patente=datos_vehiculo['patente'], defaults={'vivienda': house, 'marca': datos_vehiculo['marca'], 'modelo': datos_vehiculo['modelo'], 'color': datos_vehiculo['color']}
            )
        self.stdout.write(self.style.SUCCESS('Datos aleatorios cargados en sistema B con Faker.'))
