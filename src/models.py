import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def modelos_area_conocimiento(df):
    # Debido al desbalance de clases del dataset, además de accuracy se
    # utilizaran métricas como precision, recall y F1-score para evaluar
    # el desempeño real del modelo.

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

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    # verificamos dimensiones
    print(X_train.shape)
    print(X_test.shape)

    # Creamos modelo de regresion logistica
    modelo_log = LogisticRegression(
        max_iter=1000
    )

    # entrenamos el modelo
    modelo_log.fit(X_train, Y_train)

    # hacemos predicciones
    pred_log = modelo_log.predict(X_test)

    # Hacemos evaluacion
    print("=== REGRESIÓN LOGÍSTICA ===")

    print(
        "Accuracy:",
        accuracy_score(Y_test, pred_log)
    )

    print(
        "Precision:",
        precision_score(
            Y_test,
            pred_log,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "Recall:",
        recall_score(
            Y_test,
            pred_log,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "F1-score:",
        f1_score(
            Y_test,
            pred_log,
            average="weighted",
            zero_division=0
        )
    )

    # Creamos el modelo de Arbol
    modelo_tree = DecisionTreeClassifier(
        random_state=42
    )

    # Entrenamos
    modelo_tree.fit(X_train, Y_train)

    # Aplicamos predicciones
    pred_tree = modelo_tree.predict(X_test)

    print("=== ÁRBOL DE DECISIÓN ===")

    print(
        "Accuracy:",
        accuracy_score(Y_test, pred_tree)
    )

    print(
        "Precision:",
        precision_score(
            Y_test,
            pred_tree,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "Recall:",
        recall_score(
            Y_test,
            pred_tree,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "F1-score:",
        f1_score(
            Y_test,
            pred_tree,
            average="weighted",
            zero_division=0
        )
    )

    # verificamos si hubo overfitting
    train_pred_tree = modelo_tree.predict(X_train)

    train_accuracy = accuracy_score(
        Y_train,
        train_pred_tree
    )

    print(
        "Accuracy entrenamiento:",
        train_accuracy
    )

    test_accuracy = accuracy_score(
        Y_test,
        pred_tree
    )

    print(
        "Accuracy prueba:",
        test_accuracy
    )


def modelos_pais(df):
    print(
        df["País"].value_counts().head(10)
    )

    top_paises = df["País"].value_counts().head(10).index

    df["País"] = df["País"].apply(
        lambda x: x if x in top_paises else "OTROS"
    )

    # XGBoost NO acepta texto directamente en y
    # Creamos el encoder
    encoder_y = LabelEncoder()

    y_encoded = encoder_y.fit_transform(df["País"])

    X = df[
        [
            "Área Conocimiento",
            "Nivel Académico",
            "Edad (años)",
            "Sexo",
            "Estado civil"
        ]
    ]

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    # Creamos nuevo split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.2,
        random_state=42,
        stratify=y_encoded
    )

    # Random Forest
    modelo_rf = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )

    modelo_rf.fit(X_train, y_train)

    pred_rf = modelo_rf.predict(X_test)

    print("=== RANDOM FOREST ===")

    print(
        "Accuracy:",
        accuracy_score(y_test, pred_rf)
    )

    print(
        "Precision:",
        precision_score(
            y_test,
            pred_rf,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "Recall:",
        recall_score(
            y_test,
            pred_rf,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "F1-score:",
        f1_score(
            y_test,
            pred_rf,
            average="weighted",
            zero_division=0
        )
    )

    # verificamos overfitting RF
    train_pred_rf = modelo_rf.predict(X_train)

    train_accuracy_rf = accuracy_score(
        y_train,
        train_pred_rf
    )

    print(
        "Accuracy entrenamiento RF:",
        train_accuracy_rf
    )

    test_accuracy_rf = accuracy_score(
        y_test,
        pred_rf
    )

    print(
        "Accuracy prueba RF:",
        test_accuracy_rf
    )

    # Creamos el modelo XGBoost
    modelo_xgb = XGBClassifier(
        n_estimators=100,
        max_depth=8,
        learning_rate=0.1,
        random_state=42,
        n_jobs=-1
    )

    # Entrenamos
    modelo_xgb.fit(X_train, y_train)

    pred_xgb = modelo_xgb.predict(X_test)

    print("=== XGBOOST ===")

    print(
        "Accuracy:",
        accuracy_score(y_test, pred_xgb)
    )

    print(
        "Precision:",
        precision_score(
            y_test,
            pred_xgb,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "Recall:",
        recall_score(
            y_test,
            pred_xgb,
            average="weighted",
            zero_division=0
        )
    )

    print(
        "F1-score:",
        f1_score(
            y_test,
            pred_xgb,
            average="weighted",
            zero_division=0
        )
    )
