from pydantic import BaseModel


class PrediccionRespuesta(BaseModel):
    etiqueta: str
    confianza: float


class RegistroRespuesta(BaseModel):
    id: str
    fecha: str
    datos: dict[str, float | str]
    etiqueta: str
    confianza: float