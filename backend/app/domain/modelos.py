from dataclasses import dataclass

# Valores que puede traer un campo: número o texto
Valor = float | str


@dataclass(frozen=True)
class Entrada:
    """Datos que el usuario envía para predecir: {clave: valor}."""
    datos: dict[str, Valor]


@dataclass(frozen=True)
class Prediccion:
    """Lo que responde el modelo."""
    etiqueta: str     # clase predicha
    confianza: float  # de 0 a 1


@dataclass(frozen=True)
class Registro:
    """Una predicción guardada en el historial."""
    id: str
    fecha: str
    datos: dict[str, Valor]
    etiqueta: str
    confianza: float


class EntradaInvalida(Exception):
    """Los datos no sirven para predecir (faltan o tienen otro tipo)."""