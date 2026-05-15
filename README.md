# proyecto-ciencia-de-datos

## Descripción

Este proyecto de ciencia de datos tiene como objetivo Desarrollar modelos de machine learning capaces de identificar las áreas profesionales con mayor proyección internacional o con mayor presencia migratoria internacional para los colombianos, utilizando variables sociodemográficas y académicas provenientes de registros migratorios.

## Integrantes
- Nelson Garnica
- Alvaro Guevara
- Juan Cruz

## Dataset
- Fuente: Datos.gov.co
- Nombre Dataset: Migración colombianos a Canadá, Estados Unidos, Sudáfrica y Australia
- Link: datos.gov.co/Estad-sticas-Nacionales/Migraci-n-colombianos-a-Canad-Estados-Unidos-Sud-f/j8zm-8ebe
- Variables Categoricas: país, nivel academico, área de conocimiento, sexo. 
- Variables Numericas: edad, año.

### Importante
para cargar el dataset en tu maquina localmente, descarga el dataset del link completo y guardalo en una sub carpeta dentro del proyecto llamada: "data", este archivo no se puede subir a github debido a que **pesa mas de lo permitido**

## Tecnologias
- Python · Visual Studio Code · StreamLit · Git · GitHub 


## Modelo elegido: Random Forest
### ¿Por que?

Elegir Random Forest es la decisión mas estrategica por que actua como un comite que equilibra precisión y versatibilidad debido a que el Dataset maneja Variables Categoricas y numericas, ademas de relaciones no lienales, puede existir ruido en el dataset por su gran tamaño (+ 1'000.000 de datos) y puede haber variables atípicas a demas de manejar mejor las relaciones complejas, este modelo ofrece la potencia necesaria para resolver el problema sin sacrificar claridad ni entendimiento.

### por que no otros

A pesar de que existen otras herramientas populares en la ciencia de datos, para este proyecto en particular presentan limitaciones que las dejan fuera de juego. Por un lado, opciones como el Árbol de Decisión o la Regresión Logística pecan de ser demasiado simples; el primero tiende a memorizar los datos en lugar de aprender patrones generales (overfitting), mientras que la segunda asume que todo se puede separar con una línea recta, ignorando las relaciones complejas que suelen tener variables como el país o el nivel académico.

Por otro lado, la Regresión Lineal queda descartada por una cuestión de concepto fundamental: está diseñada para predecir valores numéricos continuos (como el precio de una casa) y no para clasificar categorías. Finalmente, aunque algoritmos como XGBoost ofrecen un rendimiento técnico superior, su complejidad los convierte en una "caja negra" difícil de calibrar y explicar, sin embargo no se descarta que sea una opcion mas viable que Random Forest.

## Comparación

Compararemos 3 modelos distintos:
1. Árbol de Decisión
2. Regresión Logistica
3. Random Forest
4. XGBoost

## Variable Objetivo

- Area_Conocimiento

## Variables predictorias

- País
- Edad
- Nivel Académico
- Sexo
- Estado civil

## Cambios:

- Se filtraron registros de personas menores de edad debido a que el análisis se centra en perfiles académicos y profesionales asociados a movilidad internacional.
- Debido al desbalance de clases del dataset, además de accuracy se utilizaron métricas como precision, recall y F1-score para evaluar el desempeño real del modelo.