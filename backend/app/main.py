from pathlib import Path

from app.adapters.entrada.api import crear_app
from app.adapters.salida.modelo_sklearn import ModeloSklearn
from app.adapters.salida.repositorio_memoria import RepositorioMemoria
from app.application.servicio_prediccion import ServicioPrediccion

# Composición: aquí (y solo aquí) se eligen los adaptadores
RAIZ = Path(__file__).resolve().parent.parent

modelo = ModeloSklearn(RAIZ / "ml" / "modelo.joblib")
servicio = ServicioPrediccion(modelo, RepositorioMemoria())
app = crear_app(servicio)