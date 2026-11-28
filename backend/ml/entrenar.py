from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Los MISMOS campos que la app (mobile/src/models/campos.ts)
CAMPOS = {"edad": "numero", "ingreso": "numero", "comentario": "texto"}
OBJETIVO = "etiqueta"
CARPETA = Path(__file__).resolve().parent

datos = pd.read_csv(CARPETA / "datos.csv")
X = datos[list(CAMPOS)]
y = datos[OBJETIVO]

numericos = [c for c, t in CAMPOS.items() if t == "numero"]
textos = [c for c, t in CAMPOS.items() if t == "texto"]
preparacion = ColumnTransformer(
    [("numeros", StandardScaler(), numericos)]
    + [(f"texto_{c}", TfidfVectorizer(), c) for c in textos]
)

pipeline = Pipeline([
    ("preparacion", preparacion),
    ("modelo", LogisticRegression(max_iter=1000)),  # cambia el algoritmo aquí
])

X_ent, X_prueba, y_ent, y_prueba = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
pipeline.fit(X_ent, y_ent)
print(classification_report(y_prueba, pipeline.predict(X_prueba)))

# Entrena con todos los datos y guarda el modelo junto con sus campos
pipeline.fit(X, y)
joblib.dump({"pipeline": pipeline, "campos": CAMPOS}, CARPETA / "modelo.joblib")
print("Modelo guardado en ml/modelo.joblib")