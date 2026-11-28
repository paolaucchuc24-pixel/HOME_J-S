from abc import ABC, abstractmethod

from app.domain.modelos import Entrada, Prediccion, Registro


class ModeloPredictivo(ABC):
    """Puerto de salida: cualquier modelo de IA que sepa predecir."""

    @abstractmethod
    def campos_requeridos(self) -> list[str]:
        """Claves que el modelo necesita para predecir."""

    @abstractmethod
    def predecir(self, entrada: Entrada) -> Prediccion:
        """Regresa la etiqueta predicha y su confianza."""


class RepositorioPredicciones(ABC):
    """Puerto de salida: dónde se guardan las predicciones."""

    @abstractmethod
    def guardar(self, registro: Registro) -> None: ...

    @abstractmethod
    def listar(self) -> list[Registro]: ...