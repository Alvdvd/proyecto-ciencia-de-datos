import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ejecutar_eda(df):
    # realizamos conteo de áreas de conocimiento
    areas = df["Área Conocimiento"].value_counts()
    print(areas)

    # Grafica de las areas mas representativas
    areas.head(10).plot(kind="bar", figsize=(12, 6))
    plt.title("Áreas con mayor migración internacional")
    plt.xlabel("Área de conocimiento")
    plt.ylabel("Cantidad de registros")
    plt.xticks(rotation=75)
    plt.show()

    # Revisamos Valores de Nivel Academico
    print(df["Nivel Académico"].value_counts())

    niveles = df["Nivel Académico"].value_counts()
    print(niveles)

    niveles.plot(kind="bar", figsize=(10, 5))
    plt.title("Niveles académicos con mayor presencia migratoria")
    plt.xlabel("Nivel académico")
    plt.ylabel("Cantidad de registros")
    plt.xticks(rotation=45)
    plt.show()

    # Relación Área <-> Nivel Académico
    cruce_area_nivel = pd.crosstab(
        df["Área Conocimiento"],
        df["Nivel Académico"]
    )
    print(cruce_area_nivel)

    plt.figure(figsize=(14, 8))
    sns.heatmap(cruce_area_nivel, cmap="Blues")
    plt.title("Relación entre Área de Conocimiento y Nivel Académico")
    plt.show()

    # Cruce País <-> Area
    cruce_pais_area = pd.crosstab(
        df["País"],
        df["Área Conocimiento"]
    )
    print(cruce_pais_area)

    plt.figure(figsize=(14, 8))
    sns.heatmap(cruce_pais_area, cmap="Blues")
    plt.title("Distribución de Áreas de Conocimiento por País")
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.hist(df["Edad (años)"], bins=30)
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

    print("Media:", df["Edad (años)"].mean())
    print("Mediana:", df["Edad (años)"].median())
    print("Moda:", df["Edad (años)"].mode()[0])

    # Paises con mayor migración
    paises = df["País"].value_counts()
    print(paises.head(10))

    paises.head(10).plot(kind="bar", figsize=(10, 5))
    plt.title("Países con mayor cantidad de migrantes")
    plt.xlabel("País")
    plt.ylabel("Cantidad de registros")
    plt.xticks(rotation=45)
    plt.show()

    # Analisis Area por pais
    top_paises = df["País"].value_counts().head(5).index

    # Filtramos dataset
    df_top = df[df["País"].isin(top_paises)]

    plt.figure(figsize=(14, 6))
    sns.countplot(data=df_top, x="País", hue="Área Conocimiento")
    plt.title("Áreas de conocimiento por país")
    plt.xticks(rotation=45)
    plt.show()

    # BOX-PLOT de edades
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df["Edad (años)"])
    plt.title("Distribución de edades")
    plt.show()

    # Distribuciones porcentuales
    porcentaje_areas = (
        df["Área Conocimiento"]
        .value_counts(normalize=True) * 100
    )
    print(porcentaje_areas)
