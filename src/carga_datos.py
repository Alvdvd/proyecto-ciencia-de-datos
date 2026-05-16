import pandas as pd


def cargar_datos(ruta):

    ruta = "data/Connacionales_inscritos_en_el_Registro_Ciudadano_en_Línea_20260514.xlsx"

    df = pd.read_excel(ruta)

    return df