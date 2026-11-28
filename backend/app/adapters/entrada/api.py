from dataclasses import asdict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.adapters.entrada.esquemas import PrediccionRespuesta, RegistroRespuesta
from app.application.servicio_prediccion import ServicioPrediccion
from app.domain.modelos import EntradaInvalida


def crear_app(servicio: ServicioPrediccion) -> FastAPI:
    """Adaptador de entrada: traduce HTTP a casos de uso."""
    app = FastAPI(title="API de predicción")
    app.add_middleware(CORSMiddleware, allow_origins=["*"],
                       allow_methods=["*"], allow_headers=["*"])

    @app.get("/health")
    def health():
        return {"estado": "ok"}

    @app.post("/predict", response_model=PrediccionRespuesta)
    def predict(datos: dict[str, float | str]):
        try:
            p = servicio.predecir(datos)
        except EntradaInvalida as e:
            raise HTTPException(status_code=422, detail=str(e))
        return PrediccionRespuesta(etiqueta=p.etiqueta, confianza=p.confianza)

    @app.get("/predicciones", response_model=list[RegistroRespuesta])
    def predicciones():
        return [RegistroRespuesta(**asdict(r)) for r in servicio.historial()]

    return app