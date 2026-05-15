import pandas as pd

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
print(df.shape)
print("------------------------------")