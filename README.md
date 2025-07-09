# Sistema de Gestión de Libros - API REST con Django

Una API REST completa para la gestión de bibliotecas digitales, desarrollada con Django y Django REST Framework. Esta aplicación permite administrar libros, autores, géneros y reseñas de usuarios, incluyendo funcionalidades avanzadas de análisis de datos.

# 🛠️ Tecnologías Utilizadas

Backend: Django 5.2.1, Django REST Framework 3.16.0

Base de Datos: PostgreSQL (configurable a SQLite)

Análisis de Datos: Pandas 2.3.0, Matplotlib 3.10.3

Autenticación: Django REST Framework Simple JWT

Lenguaje: Python 3.9+

# ⚙️ Instalación paso a paso

bash

#1. Crear entorno virtual
python -m venv env

#2. Activar entorno virtual
env\Scripts\activate

#3. Instalar dependencias
pip install django djangorestframework psycopg2-binary pandas matplotlib

#4. Crear proyecto Django
django-admin startproject login_project

#5. Crear la app principal
python manage.py startapp libros

#6. Migraciones y ejecución
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Configuración de Base de Datos

PostgreSQL:
Modificar login_project/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'libreriaanibal',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '8001', 
    }
}

# Inicialización de la Base de Datos

bash
Crear migraciones
python manage.py makemigrations

Aplicar migraciones
python manage.py migrate

Crear superusuario
python manage.py createsuperuser

# Carga de Datos de Prueba
   
bash
Asignar calificaciones (opcional)
python assign_calif.py

Asignar géneros a libros (opcional)
python assign_genres.py

# Ejecutar el Servidor
   
bash
python manage.py runserver 127.0.0.1:8001

La API estará disponible en: http://127.0.0.1:8001/api/libros/

# 🧩 ¿Cómo funciona este sistema?

   Se registran libros, autores, géneros y calificaciones.

   Se consume la API desde herramientas como Postman.

   Se exportan datos a CSV.

   Se procesan y visualizan con Pandas/Matplotlib en Google Colab o local.

   Se generan sugerencias según géneros y calificaciones.

   Soporta carga en lote desde Postman (many=True en los serializers).

# 🏗️ Arquitectura del Proyecto

Aplicaciones Principales
├── login_project/users/      # Autenticación y gestión de usuarios
├── libros/                   # Modelos y lógica de negocio principal
├── login_project/            # Configuración global del proyecto
└── scripts/                  # Scripts de carga de datos y análisis

# 🔐 Autenticación de Usuarios
La aplicación login_project/users maneja el registro y el inicio de sesión de usuarios.

![imagen](https://github.com/user-attachments/assets/e58c1944-a8a1-46b6-a9ac-6c383021df60)

![imagen](https://github.com/user-attachments/assets/7e5a2323-e6a1-4a10-9945-1e38b960ddd8)

![imagen](https://github.com/user-attachments/assets/34408c01-8d8a-4086-9e76-eee8253eab2b)

# Peticiones en Postman (Autenticación Usuarios):
![imagen](https://github.com/user-attachments/assets/b02ef1d3-812f-4f98-a9a1-c7f63abccd06)

![imagen](https://github.com/user-attachments/assets/88f2bb4e-2794-44c8-be5c-41119d9cdf1f)

# 📚 Gestión de Libros (CRUD):
La aplicacion libros sirve para la creación, edición, consulta y eliminación de libros (con sus respectivos autores, generos y calificaciones)

![imagen](https://github.com/user-attachments/assets/63d7b03c-85c9-47bb-920e-9f94549584d0)

![imagen](https://github.com/user-attachments/assets/77fb31ed-9b20-4cd3-8be3-b364f3416396)

![imagen](https://github.com/user-attachments/assets/1455de33-2783-489f-8f6a-a3e381197436)
![imagen](https://github.com/user-attachments/assets/95ed4c28-f007-4f0a-adb1-aed45054fb65)
![imagen](https://github.com/user-attachments/assets/6d1b58cc-a5f0-4e09-92b4-7dc8b618caa2)

![imagen](https://github.com/user-attachments/assets/995b627d-4af6-496c-b72b-fdad64a7a3d2)

# Peticiones en Postman (Libros):
Creación de Autor:
![imagen](https://github.com/user-attachments/assets/a104a952-f089-4cf1-aebe-6fe641f3ae37)

Creación de Genero:
![imagen](https://github.com/user-attachments/assets/53c4a087-e4ae-4ee7-bb63-4fcf83cf1ab4)

Creación de Caificación:
![imagen](https://github.com/user-attachments/assets/d9413997-abd6-4a51-8ba1-aae697753ce3)

Creación de Libro:
![imagen](https://github.com/user-attachments/assets/13eeb929-48d7-48c2-9232-b0ffeb734237)

Y luego las peticiones de para edición, consultas y eliminaciones.

# 📚 Listado de libros





# Generación y Explicación de Graficos



















