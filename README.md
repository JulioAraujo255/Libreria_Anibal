Sistema de Gestión de Libros - API REST con Django

Una API REST completa para la gestión de bibliotecas digitales, desarrollada con Django y Django REST Framework. Esta aplicación permite administrar libros, autores, géneros y reseñas de usuarios, incluyendo funcionalidades avanzadas de análisis de datos.

📋 Características Principales

Gestión Completa de Libros: Operaciones CRUD para libros, autores y géneros
Sistema de Calificaciones: Los usuarios pueden calificar y comentar libros
Autenticación JWT: Sistema seguro de autenticación con tokens
Búsqueda Avanzada: Filtros por múltiples criterios (nombre, autor, género, calificación)
Recomendaciones Inteligentes: Sugerencias basadas en calificaciones por género
Análisis de Datos: Visualizaciones con Pandas y Matplotlib
API RESTful: Endpoints bien estructurados siguiendo estándares REST

🏗️ Arquitectura del Proyecto

Aplicaciones Principales
├── login_project/users/      # Autenticación y gestión de usuarios
├── libros/                   # Modelos y lógica de negocio principal
├── login_project/            # Configuración global del proyecto
└── scripts/                  # Scripts de carga de datos y análisis

🛠️ Tecnologías Utilizadas

Backend: Django 5.2.1, Django REST Framework 3.16.0
Base de Datos: PostgreSQL (configurable a SQLite)
Análisis de Datos: Pandas 2.3.0, Matplotlib 3.10.3
Autenticación: Django REST Framework Simple JWT
Lenguaje: Python 3.9+

🚀 Instalación y Configuración

1. Preparación del Entorno
   
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate

2. Instalación de Dependencias
   
Crear un archivo requirements.txt con las siguientes dependencias:
txtasgilib==3.8.1
certifi==2025.6.15
charset-normalizer==3.4.2
contourpy==1.3.2
cycler==0.12.1
Django==5.2.1
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
fonttools==4.58.4
idna==3.10
kiwisolver==1.4.8
matplotlib==3.10.3
numpy==2.3.1
packaging==25.0
pandas==2.3.0
pillow==11.2.1
psycopg2-binary==2.9.10
PyJWT==2.9.0
pyparsing==3.2.3
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.4
six==1.17.0
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.5.0  

bashpip install -r requirements.txt

3. Configuración de Base de Datos

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

4. Inicialización de la Base de Datos

bash# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

5. Carga de Datos de Prueba
   
bash# Asignar calificaciones (opcional)
python assign_calif.py

# Asignar géneros a libros (opcional)
python assign_genres.py

6. Ejecutar el Servidor
   
bashpython manage.py runserver

La API estará disponible en: http://127.0.0.1:8001/api/libros/

📚 Estructura de Modelos

Modelo de Autor









