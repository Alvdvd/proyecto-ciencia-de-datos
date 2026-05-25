import matplotlib.pyplot as plt


def limpiar_datos(df):
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

    # Verificamos datos de edad
    plt.hist(df["Edad (años)"], bins=20)
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

    # Revision de dimensiones despues de limpieza logica para verificar
    # que no existen variables de tipo [Maestia, MAESTRIA, maestria]
    print("------------------------------")
    print(df["Nivel Académico"].unique())
    print("------------------------------")
    print(df["Sexo"].unique())
    print("------------------------------")
    print(df["Estado civil"].unique())
    print("------------------------------")
    print(df["Área Conocimiento"].unique())
    print("------------------------------")

    niveles_invalidos = [
        "SIN INFORMACIÓN",
        "NINGUNO",
        "UNIVERSITARIA"
    ]

    df = df[
        ~df["Nivel Académico"].isin(niveles_invalidos)
    ]

    print(df["Nivel Académico"].value_counts())
    # Verificamos el registro de datos
    print(df.shape)

    return df
