---
title: "Guía del laboratorio"
sidebar_position: 1
slug: /
---

Este proyecto permite seguir una petición desde una pantalla React hasta Django, y desde Django hasta otro servidor. Al terminar podrás implementar una ruta, definir su contrato JSON, consumirla desde otro proceso y verificar los cambios en la base de datos.

## Ruta de aprendizaje de API REST

Sigue las lecciones en orden. En cada una encontrarás un ejemplo resuelto, una práctica guiada y un reto para verificar que puedes aplicar lo aprendido.

1. [Reconocer un recurso, método y estado HTTP](./curso-rest/01-rest.md).
2. [Crear un endpoint con Django REST Framework](./curso-rest/02-django.md).
3. [Consumir una API desde Python](./curso-rest/03-consumir.md).
4. [Publicar un contrato para que otros clientes lo usen](./curso-rest/04-publicar.md).
5. [Conectar una interfaz React](./curso-rest/05-react.md).
6. [Proteger la API con usuario y contraseña o token](./curso-rest/06-seguridad.md).

## Procesos del laboratorio

| Proceso | Puerto de referencia | Responsabilidad |
| --- | --- | --- |
| Sistema A | 8000 | Historial de accesos vehiculares |
| Sistema B | 8001 | Padrón del condominio y APIs de práctica |
| Vite | Puerto que indique la consola | Interfaz de un frontend |
| Docusaurus | 8088 | Guía del laboratorio |

## Preparar el entorno

Desde la raíz en PowerShell, crea el entorno si aún no existe.

```powershell
python -m venv venv
& .\venv\Scripts\python.exe -m pip install -r sistema_a/requirements.txt -r sistema_b/requirements.txt
& .\venv\Scripts\python.exe sistema_a/manage.py migrate
& .\venv\Scripts\python.exe sistema_b/manage.py migrate
```

Usa bases locales de prueba para ejecutar los seeders. Cada comando escribe en la base del sistema correspondiente. Puedes crear un administrador propio con `manage.py createsuperuser`.

```powershell
& .\venv\Scripts\python.exe sistema_a/manage.py seed_data
& .\venv\Scripts\python.exe sistema_b/manage.py seed_data
# Ejecuta cada servidor en una terminal distinta.
& .\venv\Scripts\python.exe sistema_a/manage.py runserver 8000
& .\venv\Scripts\python.exe sistema_b/manage.py runserver 8001
```

El puerto forma parte de las URLs configuradas. Si lo cambias, revisa los settings de Django y las URLs de los servicios React. Empieza por los modelos de ambos sistemas.

[Comenzar con el Sistema A](./sistema-a.md) · [Consultar el Sistema B](./sistema-b.md)

[Elegir una propuesta de desarrollo](./propuestas.md)
