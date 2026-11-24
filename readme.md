# Integración de sistemas del condominio

Este proyecto contiene dos aplicaciones Django independientes que trabajan juntas para administrar un condominio o villa.

## Sistemas

### Sistema B: registro de viviendas y vehículos

El sistema B mantiene el registro principal del condominio:

- Casas o viviendas, identificadas por piso y número.
- Propietario de cada vivienda.
- Uno o varios vehículos asociados a cada casa.
- Patente, marca, modelo, color y estado del vehículo.

La información se administra desde el panel de Django Admin y se consulta mediante una API.

### Sistema A: control de acceso vehicular

El sistema A registra las entradas y salidas de vehículos de los residentes.

Cuando se intenta registrar un movimiento, el sistema A consulta la API del sistema B para verificar si la patente corresponde a un vehículo autorizado. El resultado de la consulta queda guardado junto con el movimiento.

## Estructura

```text
evaluacion 4 integraciones/
├── sistema_a/
│   ├── core/       # Modelo y administración de accesos
│   ├── api_v1/     # API para registrar entradas y salidas
│   └── sistema_a/  # Configuración del proyecto Django
├── sistema_b/
│   ├── core/       # Casas y vehículos
│   ├── api_v1/     # API de consulta de vehículos
│   └── sistema_b/  # Configuración del proyecto Django
├── frontend/       # Aplicación React/Vite
└── venv/           # Entorno virtual local, no versionado
```

## Modelos principales

### Sistema B

`House`

- `floor`: piso de la vivienda.
- `number`: número de casa.
- `owner`: propietario.

`Vehicle`

- `house`: vivienda asociada.
- `plate`: patente única.
- `brand`: marca.
- `model`: modelo.
- `color`: color.
- `active`: indica si el vehículo está autorizado.

Una vivienda puede tener varios vehículos registrados.

### Sistema A

`VehicleAccess`

- `plate`: patente consultada.
- `movement`: tipo de movimiento: `entry` o `exit`.
- `occurred_at`: fecha y hora del registro.
- `authorized`: resultado de la consulta al sistema B.
- `vehicle_data`: respuesta obtenida desde el sistema B.

## API del sistema B

Consulta un vehículo por su patente:

```http
GET http://localhost:8001/api/v1/vehicles/ABCD12/
```

Respuesta para un vehículo registrado:

```json
{
  "authorized": true,
  "plate": "ABCD12",
  "house": {
    "floor": 1,
    "number": "101",
    "owner": "Ana Pérez"
  },
  "vehicle": {
    "brand": "Toyota",
    "model": "Yaris",
    "color": "Blanco"
  }
}
```

## API del sistema A

Registra una entrada o salida:

```http
POST http://localhost:8000/api/v1/access/
Content-Type: application/json
```

Cuerpo de ejemplo:

```json
{
  "plate": "ABCD12",
  "movement": "entry"
}
```

El campo `movement` acepta los valores:

- `entry`: entrada.
- `exit`: salida.

El sistema A consulta automáticamente al sistema B usando la URL configurada en `SYSTEM_B_API_URL`.

## Instalación

Se requiere Python y un entorno virtual con Django instalado.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución del sistema B

```powershell
cd sistema_b
..\venv\Scripts\python.exe manage.py migrate
..\venv\Scripts\python.exe manage.py seed_data
..\venv\Scripts\python.exe manage.py createsuperuser
..\venv\Scripts\python.exe manage.py runserver 8001
```

Panel administrativo:

```text
http://localhost:8001/admin/
```

## Ejecución del sistema A

En otra terminal:

```powershell
cd sistema_a
..\venv\Scripts\python.exe manage.py migrate
..\venv\Scripts\python.exe manage.py seed_data
..\venv\Scripts\python.exe manage.py createsuperuser
..\venv\Scripts\python.exe manage.py runserver 8000
```

Panel administrativo:

```text
http://localhost:8000/admin/
```

Primero debe ejecutarse el sistema B en el puerto `8001`, ya que el sistema A lo consulta para validar las patentes.

## Seeders

Los comandos `seed_data` generan información aleatoria de prueba utilizando `Faker`.

En el sistema B crea casas y vehículos de ejemplo:

```powershell
python manage.py seed_data
```

En el sistema A crea un movimiento de entrada de prueba:

```powershell
python manage.py seed_data
```

## Migraciones

Para crear nuevas migraciones después de modificar los modelos:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Notas

- No se utilizan formularios personalizados; la administración se realiza mediante modelos y Django Admin.
- Las bases de datos SQLite locales están excluidas mediante `.gitignore`.
- En producción, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y `SYSTEM_B_API_URL` deben configurarse mediante variables de entorno.
