from fastapi.testclient import TestClient

from app.adapters.entrada.api import crear_app
from app.adapters.salida.modelo_falso import ModeloFalso
from app.adapters.salida.repositorio_memoria import RepositorioMemoria
from app.application.servicio_prediccion import ServicioPrediccion

cliente = TestClient(crear_app(
    ServicioPrediccion(ModeloFalso(), RepositorioMemoria())))


def test_predict_responde_etiqueta_y_confianza():
    r = cliente.post("/predict", json={
        "edad": 30, "ingreso": 20000, "comentario": "me interesa"})
    assert r.status_code == 200
    assert r.json() == {"etiqueta": "Compra", "confianza": 0.9}


def test_predict_sin_campos_responde_422():
    r = cliente.post("/predict", json={"edad": 30})
    assert r.status_code == 422


def test_historial():
    assert cliente.get("/predicciones").status_code == 200