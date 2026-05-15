import pandas as pd
import matplotlib.pyplot as plt

ruta = "data/Connacionales_inscritos_en_el_Registro_Ciudadano_en_Línea_20260514.xlsx"

df = pd.read_excel(ruta)

# Ver primeras filas
print(df.head())
print("------------------------------")

# Ver información general
print("Información General")
print(df.info())
print("------------------------------")

# Ver dimensiones
print("Dimension del dataset")
print(df.shape)
print("------------------------------")

# Ver datos nulos
print("Datos Nulos: ")
print(df.isnull().sum()) # Datos nulos = 35
print("------------------------------")

# Ver datos Duplicados
print("Datos Duplicados: ")
print(df.duplicated().sum()) # Duplicados = 0
print("------------------------------")
# No hay Datos Duplicados

# Eliminamos columnas Inutiles
columnas_eliminar = [
    "Código ISO país",
    "Localización",
    "Fecha de Registro"
]

df = df.drop(columns=columnas_eliminar)

print("Verificamos que si eliminamos las columnas inutiles")
print(df.columns)
print("------------------------------")

# Verificamos dimensiones
print("Antes de Limpieza")
print(df.shape)
print("------------------------------")

# Filtrar edades validas 
df = df[
    (df["Edad (años)"] >= 18) &
    (df["Edad (años)"] <= 100)
    ]

# Revision de dimensiones despues de limpieza logica
print("Despues de limpieza: ", df.shape)


print("------------------------------")
print(df["Nivel Académico"].unique())
print("------------------------------")
print(df["Sexo"].unique())
print("------------------------------")
print(df["Estado civil"].unique())
print("------------------------------")
print(df["Área Conocimiento"].unique())
print("------------------------------")

#Verificamos datos de edad
plt.hist(df["Edad (años)"], bins=20)

plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

plt.show()


# Aplicamos variables
X = df[
    [
        "País",
        "Edad (años)",
        "Nivel Académico",
        "Sexo",
        "Estado civil"
    ]
]

Y = df["Área Conocimiento"]

# Verificamos balance de clases
print(df["Área Conocimiento"].value_counts())