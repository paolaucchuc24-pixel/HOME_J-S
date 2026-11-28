from app.domain.modelos import Entrada, Prediccion
from app.domain.puertos import ModeloPredictivo


class ModeloFalso(ModeloPredictivo):
    """Adaptador de salida para pruebas: siempre responde lo mismo."""

    def campos_requeridos(self) -> list[str]:
        return ["edad", "ingreso", "comentario"]

    def predecir(self, entrada: Entrada) -> Prediccion:
        return Prediccion(etiqueta="Compra", confianza=0.9)