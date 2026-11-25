import { Prediccion, Registro } from "@/models/Prediccion";

// Se guarda en memoria: se borra al recargar la app
const registros: Registro[] = [];

export function guardar(p: Prediccion): void {
  registros.unshift({
    ...p,
    id: String(Date.now()),
    fecha: new Date().toLocaleTimeString(),
  });
}

export function obtenerHistorial(): Registro[] {
  return [...registros];
}