import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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

# Verificamos dimensiones Antes de Limpieza
print(df.shape)
print("------------------------------")

# Verificamos balance de la variable
print(df["Área Conocimiento"].value_counts())
print("------------------------------")

# existen demasiados datos clasificados como ninguno, no indica y no aplica
categorias_invalidas = [
    "NINGUNA",
    "NO INDICA",
    "(NO REGISTRA)"
]

df = df[~df["Área Conocimiento"].isin(categorias_invalidas)]

# Verificamos de nuevo balance de clases sin datos que no contengan nada
print(df["Área Conocimiento"].value_counts())
print("------------------------------\n")
print("Despues de limpieza: ", df.shape)

# Filtrar edades validas 
df = df[
    (df["Edad (años)"] >= 18) &
    (df["Edad (años)"] <= 100)
    ]

#Verificamos datos de edad
plt.hist(df["Edad (años)"], bins=20)

plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

plt.show()

# Revision de dimensiones despues de limpieza logica para verificar que no existen variables de tipo [Maestia, MAESTRIA, maestria]

print("------------------------------")
print(df["Nivel Académico"].unique())
print("------------------------------")
print(df["Sexo"].unique())
print("------------------------------")
print(df["Estado civil"].unique())
print("------------------------------")
print(df["Área Conocimiento"].unique())
print("------------------------------")


# Debido al desbalance de clases del dataset, además de accuracy se utilizaran métricas como precision, recall y F1-score para evaluar el desempeño real del modelo.

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

# Aplicamos one hot encoding
X = pd.get_dummies(X)
print("------------------------------")
print(X.shape)
print("------------------------------")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#verificamos dimensiones
print(X_train.shape)
print(X_test.shape)