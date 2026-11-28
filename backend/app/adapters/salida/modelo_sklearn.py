from pathlib import Path

import joblib
import pandas as pd

from app.domain.modelos import Entrada, EntradaInvalida, Prediccion
from app.domain.puertos import ModeloPredictivo


class ModeloSklearn(ModeloPredictivo):
    """Adaptador de salida: usa un modelo entrenado con scikit-learn."""

    def __init__(self, ruta: Path):
        paquete = joblib.load(ruta)
        self._pipeline = paquete["pipeline"]
        self._campos: dict[str, str] = paquete["campos"]  # clave -> tipo

    def campos_requeridos(self) -> list[str]:
        return list(self._campos)

    def predecir(self, entrada: Entrada) -> Prediccion:
        fila = {}
        for clave, tipo in self._campos.items():
            valor = entrada.datos[clave]
            if tipo == "numero":
                try:
                    fila[clave] = float(valor)
                except ValueError:
                    raise EntradaInvalida(f"{clave} debe ser un número")
            else:
                fila[clave] = str(valor)

        probabilidades = self._pipeline.predict_proba(pd.DataFrame([fila]))[0]
        i = int(probabilidades.argmax())
        return Prediccion(
            etiqueta=str(self._pipeline.classes_[i]),
            confianza=round(float(probabilidades[i]), 2),
        )