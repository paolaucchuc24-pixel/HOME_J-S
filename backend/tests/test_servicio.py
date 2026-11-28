import pytest

from app.adapters.salida.modelo_falso import ModeloFalso
from app.adapters.salida.repositorio_memoria import RepositorioMemoria
from app.application.servicio_prediccion import ServicioPrediccion
from app.domain.modelos import EntradaInvalida

DATOS = {"edad": 30, "ingreso": 20000, "comentario": "me interesa"}


def crear_servicio():
    return ServicioPrediccion(ModeloFalso(), RepositorioMemoria())


def test_predice_y_guarda_en_historial():
    servicio = crear_servicio()
    p = servicio.predecir(DATOS)
    assert p.etiqueta == "Compra"
    assert len(servicio.historial()) == 1


def test_faltan_campos():
    with pytest.raises(EntradaInvalida):
        crear_servicio().predecir({"edad": 30})