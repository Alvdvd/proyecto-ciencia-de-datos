# proyecto-ciencia-de-datos

## Descripción

Este proyecto de ciencia de datos tiene como objetivo analizar patrones de movilidad internacional de colombianos registrados en el exterior, identificando las áreas de conocimiento con mayor presencia migratoria y explorando relaciones entre variables sociodemográficas, académicas y migratorias mediante técnicas de análisis de datos y machine learning.

## Integrantes
- Nelson Garnica
- Alvaro Guevara
- Juan Cruz

## Dataset
- Fuente: Datos.gov.co
- Nombre Dataset: Migración colombianos a Canadá, Estados Unidos, Sudáfrica y Australia
- Link: datos.gov.co/Estad-sticas-Nacionales/Migraci-n-colombianos-a-Canad-Estados-Unidos-Sud-f/j8zm-8ebe

### Variables categóricas
- País
- Nivel académico
- Área de conocimiento
- Sexo
- Estado civil
- Ciudad de residencia
- Pertenencia étnica

### Variables numéricas
- Edad
- Cantidad de personas

### Importante
Para cargar el dataset localmente, descarga el archivo desde el enlace oficial y guárdalo dentro de una subcarpeta llamada `data/`. El archivo no se encuentra en el repositorio debido a restricciones de tamaño en GitHub.

## Tecnologías
- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

# Enfoque metodológico

Inicialmente el proyecto fue planteado como un problema de clasificación multiclase orientado a predecir el área de conocimiento de los migrantes colombianos a partir de variables sociodemográficas y académicas.

Sin embargo, durante el desarrollo y entrenamiento de modelos como Regresión Logística, Árbol de Decisión y Random Forest, se identificó una baja capacidad predictiva debido al alto solapamiento entre categorías, el desbalance de clases y la limitada relación entre las variables disponibles y el objetivo planteado.

A partir de estos resultados, el enfoque del proyecto fue replanteado hacia un análisis de patrones migratorios y tendencias académicas, utilizando los modelos de machine learning como herramientas complementarias de exploración y comparación.

---

# Modelos evaluados

Se compararán distintos modelos de clasificación para analizar el comportamiento del dataset:

1. Regresión Logística
2. Árbol de Decisión
3. Random Forest
4. XGBoost

## ¿Por qué Random Forest?

Random Forest fue seleccionado como uno de los modelos principales debido a su capacidad para manejar variables categóricas y numéricas, reducir overfitting y capturar relaciones no lineales presentes en datasets complejos y desbalanceados.

Además, permite obtener resultados interpretables y comparables frente a otros modelos más simples o más complejos.

---

# Variables utilizadas

## Variable analizada inicialmente
- Área de conocimiento

## Variables predictoras
- País
- Edad
- Nivel académico
- Sexo
- Estado civil

---

# Cambios y decisiones metodológicas

- Se eliminaron registros con edades inconsistentes o fuera del rango de análisis definido.
- Se filtraron registros de personas menores de edad debido al enfoque académico y profesional del proyecto.
- Se eliminaron categorías inválidas como “NINGUNA”, “NO INDICA” y “(NO REGISTRA)” en el área de conocimiento.
- Debido al desbalance de clases del dataset, además de accuracy se utilizaron métricas como precision, recall y F1-score.
- Los resultados obtenidos evidenciaron limitaciones predictivas importantes, lo que llevó al replanteamiento metodológico del proyecto hacia análisis migratorio y tendencias académicas.