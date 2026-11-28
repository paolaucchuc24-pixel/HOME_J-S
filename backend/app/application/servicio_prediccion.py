from datetime import datetime
from uuid import uuid4

from app.domain.modelos import Entrada, EntradaInvalida, Prediccion, Registro, Valor
from app.domain.puertos import ModeloPredictivo, RepositorioPredicciones


class ServicioPrediccion:
    """Casos de uso: predecir y consultar el historial.

    Solo conoce los puertos; no sabe si el modelo es scikit-learn
    ni si el historial está en memoria o en una base de datos.
    """

    def __init__(self, modelo: ModeloPredictivo,
                 repositorio: RepositorioPredicciones):
        self._modelo = modelo
        self._repositorio = repositorio

    def predecir(self, datos: dict[str, Valor]) -> Prediccion:
        faltan = [c for c in self._modelo.campos_requeridos() if c not in datos]
        if faltan:
            raise EntradaInvalida(f"Faltan campos: {', '.join(faltan)}")

        prediccion = self._modelo.predecir(Entrada(datos))

        self._repositorio.guardar(Registro(
            id=uuid4().hex,
            fecha=datetime.now().isoformat(timespec="seconds"),
            datos=datos,
            etiqueta=prediccion.etiqueta,
            confianza=prediccion.confianza,
        ))
        return prediccion

    def historial(self) -> list[Registro]:
        return self._repositorio.listar()