from app.domain.modelos import Registro
from app.domain.puertos import RepositorioPredicciones


class RepositorioMemoria(RepositorioPredicciones):
    """Adaptador de salida: guarda en una lista (se borra al reiniciar)."""

    def __init__(self):
        self._registros: list[Registro] = []

    def guardar(self, registro: Registro) -> None:
        self._registros.insert(0, registro)

    def listar(self) -> list[Registro]:
        return list(self._registros)