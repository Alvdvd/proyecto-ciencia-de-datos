from sklearn.model_selection import train_test_split
import pandas as pd


def preparar_datos(df):

    X = df[
        [
            "Área Conocimiento",
            "Nivel Académico",
            "Edad (años)",
            "Sexo",
            "Estado civil"
        ]
    ]

    y = df["País"]

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y