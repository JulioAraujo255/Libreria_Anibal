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
