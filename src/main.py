import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

from src.load_data import cargar_datos
from src.clean_data import limpiar_datos
from src.eda import ejecutar_eda
from src.models import modelos_area_conocimiento, modelos_pais


# Ruta al dataset — cambia esto por la ruta en tu equipo
ruta = r"data/Connacionales_inscritos_en_el_Registro_Ciudadano_en_Línea_20260514.xlsx"

df = cargar_datos(ruta)
df = limpiar_datos(df)
ejecutar_eda(df)
modelos_area_conocimiento(df)
modelos_pais(df)
