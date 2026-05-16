def eliminar_columnas(df):

    columnas_eliminar = [
        "Código ISO país",
        "Ciudad de Residencia",
        "Oficina de circunscripción consular",
        "Ciudad de Nacimiento",
        "Localización",
        "Fecha de Registro"
    ]

    df = df.drop(columns=columnas_eliminar)

    return df

def filtrar_edades(df):

    df = df[
        (df["Edad (años)"] >= 18)
        &
        (df["Edad (años)"] <= 100)
    ]

    return df

def limpiar_nivel_academico(df):

    niveles_invalidos = [
        "SIN INFORMACIÓN",
        "NINGUNO",
        "UNIVERSITARIA"
    ]

    df = df[
        ~df["Nivel Académico"].isin(niveles_invalidos)
    ]

    return df