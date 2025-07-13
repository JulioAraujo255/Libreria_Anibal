# Sistema de Gestión de Libros - API REST con Django

Una API REST completa para la gestión de bibliotecas digitales, desarrollada con Django y Django REST Framework. Esta aplicación permite administrar libros, autores, géneros y reseñas de usuarios, incluyendo funcionalidades avanzadas de análisis de datos.

#  Tecnologías Utilizadas

Backend: Django 5.2.1, Django REST Framework 3.16.0

Base de Datos: PostgreSQL 

Análisis de Datos: Pandas 2.3.0, Matplotlib 3.10.3

Autenticación: Django REST Framework Simple JWT

Lenguaje: Python 3.9+

#  Instalación paso a paso

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
python manage.py runserver 127.0.0.1:8001 (Postman)

La API estará disponible en: http://127.0.0.1:8001/api/libros/

# ¿Cómo funciona este sistema?

   Se registran libros, autores, géneros y calificaciones.

   Se consume la API desde herramientas como Postman.

   Se exportan datos a CSV.

   Se procesan y visualizan con Pandas/Matplotlib en Google Colab o local.

   Se generan sugerencias según géneros y calificaciones.

   Soporta carga en lote desde Postman (many=True en los serializers).

# Arquitectura del Proyecto

Aplicaciones Principales

├── login_project/users/      # Autenticación y gestión de usuarios

├── libros/                   # Modelos y lógica de negocio principal

├── login_project/            # Configuración global del proyecto

└── scripts/                  # Scripts de carga de datos y análisis

# Autenticación de Usuarios

La aplicación login_project/users se encarga del registro y la consulta del perfil del usuario autenticado. Para ello se implementan dos vistas principales usando Django REST Framework:

El serializador define qué campos del modelo User serán visibles:

![imagen](https://github.com/user-attachments/assets/e58c1944-a8a1-46b6-a9ac-6c383021df60)

👤 RegisterView

Permite registrar nuevos usuarios.

 Se basa en el modelo incorporado User de Django.

Utiliza permisos AllowAny para que cualquier persona pueda acceder a esta vista sin autenticarse.

 Hereda de CreateAPIView, por lo que acepta solicitudes POST para registrar nuevos usuarios.

🔐 ProfileView

Requiere autenticación (IsAuthenticated) mediante tokens JWT.

Permite al usuario autenticado consultar sus propios datos (como id, username, email, etc.).

Retorna los datos serializados con UserSerializer.
    
![imagen](https://github.com/user-attachments/assets/7e5a2323-e6a1-4a10-9945-1e38b960ddd8)

Define las rutas relacionadas a usuarios:

![imagen](https://github.com/user-attachments/assets/34408c01-8d8a-4086-9e76-eee8253eab2b)

# Peticiones en Postman (Autenticación Usuarios):

![imagen](https://github.com/user-attachments/assets/b02ef1d3-812f-4f98-a9a1-c7f63abccd06)

![imagen](https://github.com/user-attachments/assets/88f2bb4e-2794-44c8-be5c-41119d9cdf1f)

# Gestión de Libros (CRUD):

El proyecto cuenta con una API REST completa que permite crear, leer, actualizar y eliminar datos de libros, autores, géneros y calificaciones. Todo esto se gestiona mediante ModelViewSet de Django REST Framework, lo que permite automatizar gran parte del trabajo.

Define las estructuras de datos:

Autor: nombre y nacionalidad del autor.

Genero: categoría o estilo literario.

Calificacion: puntaje del libro (1 a 10) y un comentario opcional.

Libro: tiene título, autor, género y una calificación.
    
![imagen](https://github.com/user-attachments/assets/63d7b03c-85c9-47bb-920e-9f94549584d0)

Permiten convertir los modelos en JSON para trabajar con la API.
Se aplican a todos los modelos (Autor, Genero, Libro, Calificacion).

![imagen](https://github.com/user-attachments/assets/77fb31ed-9b20-4cd3-8be3-b364f3416396)

Usamos ModelViewSet para tener el CRUD completo automáticamente (GET, POST, PUT, DELETE). Además, personalizamos el método create() para permitir cargas masivas de datos (listas de objetos).
Esto se replica para Autor, Genero y Calificacion.

![imagen](https://github.com/user-attachments/assets/1455de33-2783-489f-8f6a-a3e381197436)
![imagen](https://github.com/user-attachments/assets/95ed4c28-f007-4f0a-adb1-aed45054fb65)
![imagen](https://github.com/user-attachments/assets/6d1b58cc-a5f0-4e09-92b4-7dc8b618caa2)

Utiliza un DefaultRouter que registra automáticamente las rutas de cada recurso:

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

# Listado de libros

GET =  http://127.0.0.1:8001/api/libros/
    
     [
    {
        "id": 1,
        "titulo": "1984",
        "autor": 1,
        "genero": 1,
        "calificacion": 1
    },
    {
        "id": 2,
        "titulo": "Rebelión en la granja",
        "autor": 1,
        "genero": 1,
        "calificacion": 2
    },
    {
        "id": 3,
        "titulo": "It",
        "autor": 2,
        "genero": 2,
        "calificacion": 3
    },
    {
        "id": 4,
        "titulo": "El resplandor",
        "autor": 2,
        "genero": 2,
        "calificacion": 4
    },
    {
        "id": 5,
        "titulo": "Cementerio de animales",
        "autor": 2,
        "genero": 2,
        "calificacion": 5
    },
    {
        "id": 6,
        "titulo": "Asesinato en el Orient Express",
        "autor": 3,
        "genero": 2,
        "calificacion": 6
    },
    {
        "id": 7,
        "titulo": "Diez negritos",
        "autor": 3,
        "genero": 2,
        "calificacion": 7
    },
    {
        "id": 8,
        "titulo": "El asesinato de Roger Ackroyd",
        "autor": 3,
        "genero": 2,
        "calificacion": 8
    },
    {
        "id": 9,
        "titulo": "Estudio en escarlata",
        "autor": 4,
        "genero": 2,
        "calificacion": 9
    },
    {
        "id": 10,
        "titulo": "El sabueso de los Baskerville",
        "autor": 4,
        "genero": 2,
        "calificacion": 10
    },
    {
        "id": 11,
        "titulo": "El cuervo",
        "autor": 5,
        "genero": 5,
        "calificacion": 1
    },
    {
        "id": 12,
        "titulo": "Los crímenes de la calle Morgue",
        "autor": 5,
        "genero": 5,
        "calificacion": 2
    },
    {
        "id": 13,
        "titulo": "El corazón delator",
        "autor": 5,
        "genero": 5,
        "calificacion": 3
    },
    {
        "id": 14,
        "titulo": "El psicoanalista",
        "autor": 6,
        "genero": 2,
        "calificacion": 4
    },
    {
        "id": 15,
        "titulo": "La historia del loco",
        "autor": 6,
        "genero": 2,
        "calificacion": 5
    },
    {
        "id": 16,
        "titulo": "Personas desconocidas",
        "autor": 6,
        "genero": 2,
        "calificacion": 6
    },
    {
        "id": 17,
        "titulo": "Hábitos atómicos",
        "autor": 7,
        "genero": 3,
        "calificacion": 7
    },
    {
        "id": 18,
        "titulo": "Más claro, imposible",
        "autor": 7,
        "genero": 3,
        "calificacion": 8
    },
    {
        "id": 19,
        "titulo": "La vida del cosmos",
        "autor": 8,
        "genero": 3,
        "calificacion": 9
    },
    {
        "id": 20,
        "titulo": "Cosmos",
        "autor": 8,
        "genero": 3,
        "calificacion": 10
    },
    {
        "id": 21,
        "titulo": "Los mejores cuentos",
        "autor": 9,
        "genero": 4,
        "calificacion": 1
    },
    {
        "id": 22,
        "titulo": "La poesía no se vende",
        "autor": 9,
        "genero": 4,
        "calificacion": 2
    },
    {
        "id": 23,
        "titulo": "Mario Halley Mora y su tiempo",
        "autor": 10,
        "genero": 4,
        "calificacion": 3
    },
    {
        "id": 24,
        "titulo": "Historia del Paraguay",
        "autor": 10,
        "genero": 4,
        "calificacion": 4
    },
    {
        "id": 25,
        "titulo": "Joyland",
        "autor": 2,
        "genero": 2,
        "calificacion": 5
    },
    {
        "id": 26,
        "titulo": "Carrie",
        "autor": 2,
        "genero": 2,
        "calificacion": 6
    },
    {
        "id": 27,
        "titulo": "Misery",
        "autor": 2,
        "genero": 2,
        "calificacion": 7
    },
    {
        "id": 28,
        "titulo": "Christine",
        "autor": 2,
        "genero": 2,
        "calificacion": 8
    },
    {
        "id": 29,
        "titulo": "El ciclo del hombre lobo",
        "autor": 2,
        "genero": 2,
        "calificacion": 9
    },
    {
        "id": 30,
        "titulo": "Noche eterna",
        "autor": 3,
        "genero": 2,
        "calificacion": 10
    },
    {
        "id": 31,
        "titulo": "La casa torcida",
        "autor": 3,
        "genero": 2,
        "calificacion": 1
    },
    {
        "id": 32,
        "titulo": "Testigo de cargo",
        "autor": 3,
        "genero": 2,
        "calificacion": 2
    },
    {
        "id": 33,
        "titulo": "El archivo de Sherlock Holmes",
        "autor": 4,
        "genero": 2,
        "calificacion": 3
    },
    {
        "id": 34,
        "titulo": "El signo de los cuatro",
        "autor": 4,
        "genero": 2,
        "calificacion": 4
    },
    {
        "id": 35,
        "titulo": "Annabel Lee",
        "autor": 5,
        "genero": 5,
        "calificacion": 5
    },
    {
        "id": 36,
        "titulo": "La caída de la casa Usher",
        "autor": 5,
        "genero": 5,
        "calificacion": 6
    },
    {
        "id": 37,
        "titulo": "El gato negro",
        "autor": 5,
        "genero": 5,
        "calificacion": 7
    },
    {
        "id": 38,
        "titulo": "Jaque al psicoanalista",
        "autor": 6,
        "genero": 2,
        "calificacion": 8
    },
    {
        "id": 39,
        "titulo": "Un final perfecto",
        "autor": 6,
        "genero": 2,
        "calificacion": 9
    },
    {
        "id": 40,
        "titulo": "El estudiante",
        "autor": 6,
        "genero": 2,
        "calificacion": 10
    },
    {
        "id": 41,
        "titulo": "Cartas a un joven científico",
        "autor": 8,
        "genero": 3,
        "calificacion": 1
    },
    {
        "id": 42,
        "titulo": "Miles de millones",
        "autor": 8,
        "genero": 3,
        "calificacion": 2
    },
    {
        "id": 43,
        "titulo": "Divulgación y pensamiento",
        "autor": 8,
        "genero": 3,
        "calificacion": 3
    },
    {
        "id": 44,
        "titulo": "Antología poética",
        "autor": 9,
        "genero": 4,
        "calificacion": 4
    },
    {
        "id": 45,
        "titulo": "La muralla robada",
        "autor": 9,
        "genero": 4,
        "calificacion": 5
    },
    {
        "id": 46,
        "titulo": "Crónica de una nación",
        "autor": 10,
        "genero": 4,
        "calificacion": 6
    },
    {
        "id": 47,
        "titulo": "El visitante",
        "autor": 2,
        "genero": 2,
        "calificacion": 7
    },
    {
        "id": 48,
        "titulo": "Doctor Sueño",
        "autor": 2,
        "genero": 2,
        "calificacion": 8
    },
    {
        "id": 49,
        "titulo": "Billy Summers",
        "autor": 2,
        "genero": 2,
        "calificacion": 9
    },
    {
        "id": 50,
        "titulo": "El hombre del traje negro",
        "autor": 2,
        "genero": 2,
        "calificacion": 10
    },
    {
        "id": 51,
        "titulo": "Navidades trágicas",
        "autor": 3,
        "genero": 2,
        "calificacion": 1
    },
    {
        "id": 52,
        "titulo": "Muerte en el Nilo",
        "autor": 3,
        "genero": 2,
        "calificacion": 2
    },
    {
        "id": 53,
        "titulo": "Cita con la muerte",
        "autor": 3,
        "genero": 2,
        "calificacion": 3
    },
    {
        "id": 54,
        "titulo": "Historias del Paraguay profundo",
        "autor": 10,
        "genero": 4,
        "calificacion": 4
    },
    {
        "id": 55,
        "titulo": "El paraguayo, ese gran desconocido",
        "autor": 10,
        "genero": 4,
        "calificacion": 5
    },
    {
        "id": 56,
        "titulo": "Costumbres del interior",
        "autor": 10,
        "genero": 4,
        "calificacion": 6
    },
    {
        "id": 57,
        "titulo": "Ecos del silencio",
        "autor": 9,
        "genero": 4,
        "calificacion": 7
    },
    {
        "id": 58,
        "titulo": "Más allá del tiempo",
        "autor": 8,
        "genero": 3,
        "calificacion": 8
    },
    {
        "id": 59,
        "titulo": "Teoría del todo",
        "autor": 8,
        "genero": 3,
        "calificacion": 9
    },
    {
        "id": 60,
        "titulo": "Mensajes del cosmos",
        "autor": 8,
        "genero": 3,
        "calificacion": 10
    },
    {
        "id": 61,
        "titulo": "Reflejos del alma",
        "autor": 9,
        "genero": 4,
        "calificacion": 1
    },
    {
        "id": 62,
        "titulo": "Sombras del pasado",
        "autor": 10,
        "genero": 4,
        "calificacion": 2
    },
    {
        "id": 63,
        "titulo": "La ruta del jaguar",
        "autor": 10,
        "genero": 4,
        "calificacion": 3
    },
    {
        "id": 64,
        "titulo": "Viaje a las estrellas",
        "autor": 8,
        "genero": 3,
        "calificacion": 4
    },
    {
        "id": 65,
        "titulo": "En el corazón del Paraguay",
        "autor": 10,
        "genero": 4,
        "calificacion": 5
    },
    {
        "id": 66,
        "titulo": "Mario Halley Mora y el alma nacional",
        "autor": 10,
        "genero": 4,
        "calificacion": 6
    }
]

# 📄 Script de exportación y análisis

    exportar_libros.py
    import pandas as pd
    from libros.models import Libro

    data = [{
    "titulo": libro.titulo,
    "autor": libro.autor.nombre,
    "genero": libro.genero.nombre if libro.genero else None,
    "calificacion": libro.calificacion.puntaje if libro.calificacion else None
    } for libro in Libro.objects.all()]

    df = pd.DataFrame(data)
    df.to_csv("libros.csv", index=False)

# 📊 Análisis y gráficos 

    import pandas as pd
    import matplotlib.pyplot as plt

    # Leer el archivo exportado
    df = pd.read_csv("LibrosAnibal.csv")

    # Estilo visual
    plt.style.use('ggplot')

    ###  1. ¿Qué libro tiene la mejor calificación?
    mejor_libro = df[df['calificacion'] == df['calificacion'].max()]
    print("\n Libro con mejor calificación:")
    print(mejor_libro[['titulo', 'calificacion']])

    # Gráfico de barras
    plt.figure(figsize=(6,4))
    plt.bar(mejor_libro['titulo'], mejor_libro['calificacion'], color='green')
    plt.title(" Libro con mejor calificación")
    plt.ylabel("Calificación")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    ###  2. ¿Cuál es el género favorito (más frecuente)?
    genero_favorito = df['genero'].value_counts()
    print("\n Géneros más frecuentes:")
    print(genero_favorito)

    # Gráfico de pastel
    plt.figure(figsize=(6,6))
    genero_favorito.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title(" Distribución de Géneros")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    ###  3. ¿Qué autor tiene más libros?
    autor_popular = df['autor'].value_counts()
    print("\n Autores con más libros:")
    print(autor_popular)

    # Gráfico de barras
    plt.figure(figsize=(8,5))
    autor_popular.plot(kind='bar', color='orange')
    plt.title(" Autores con más libros")
    plt.ylabel("Cantidad de libros")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    ###  4. ¿Cuál es el promedio de calificaciones por autor?
    promedio_por_autor = df.groupby('autor')['calificacion'].mean().sort_values(ascending=False)
    print("\n Promedio de calificación por autor:")
    print(promedio_por_autor)
    
    # Gráfico de líneas
    plt.figure(figsize=(8,5))
    promedio_por_autor.plot(kind='line', marker='o', color='blue')
    plt.title(" Promedio de calificación por autor")
    plt.ylabel("Promedio")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    ###  5. Distribución de calificaciones (histograma)
    plt.figure(figsize=(6,4))
    df['calificacion'].plot(kind='hist', bins=5, color='purple', rwidth=0.9)
    plt.title(" Distribución de Calificaciones")
    plt.xlabel("Puntaje")
    plt.tight_layout()
    plt.show()
    
¿Qué hace este script?

Analiza qué libro tiene el mejor puntaje.

Muestra gráficos de barras, gráficos de pastel, líneas y histogramas.

Incluye insights como:

Género más frecuente

Autor con más libros

Promedio de calificación por autor

Distribución general de calificaciones

Se ejecuta desde la terminal con el script: python graficos_libros.py

![Grafico_1](https://github.com/user-attachments/assets/7971669b-164e-4a60-93da-33d52cffdc05)

![Grafico_2](https://github.com/user-attachments/assets/009ea643-f8f4-48a8-ac96-dcb7b4eb84fa)

![Grafico_3](https://github.com/user-attachments/assets/71a01d1b-55d4-49c3-93d1-665e52bf6111)

![Grafico_4](https://github.com/user-attachments/assets/b21a1f93-a27c-4bd3-b21d-cb8d67b320fd)

![Grafico_5](https://github.com/user-attachments/assets/babc6750-bb9e-40ed-b3f7-c893ca35a85e)

# Libros con mejor valoración 

Cuando el usuario pase un id de género (por ejemplo, genero_id=1), el sistema debe devolver los mejores libros (por ejemplo, puntaje ≥ 4) de ese género ordenados por calificación.

Se agrego al proyecto:

libros/urls.py:

urlpatterns = [
    path('sugerencias/<int:genero_id>/', sugerencias_por_genero, name='sugerencias-por-genero'),
]

libros/views.py:

@api_view(['GET'])
def sugerencias_por_genero(request, genero_id):
    libros = Libro.objects.filter(
        genero=genero_id,
        calificacion__puntaje__gte=5  # Filtramos por calificación ≥ 5
    ).order_by('-calificacion__puntaje')
    
Uso en Postman: http://127.0.0.1:8000/api/sugerencias/2/

Resultado:

[
    {
        "id": 4,
        "titulo": "El resplandor",
        "autor": 2,
        "genero": 2,
        "calificacion": 4
    },
    {
        "id": 14,
        "titulo": "El psicoanalista",
        "autor": 6,
        "genero": 2,
        "calificacion": 4
    },
    {
        "id": 34,
        "titulo": "El signo de los cuatro",
        "autor": 4,
        "genero": 2,
        "calificacion": 4
    },
]

# Licencias de herramientas usadas

![imagen](https://github.com/user-attachments/assets/2b9fe8bb-126a-4808-bcb9-049e52a00f46)





    

















