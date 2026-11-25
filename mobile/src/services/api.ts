import { Entrada, Prediccion } from "@/models/Prediccion";

// PASO 2: respuesta simulada.
// Cuando el backend esté listo, este archivo usará fetch.
const ETIQUETAS = ["Clase A", "Clase B", "Clase C"]; // cámbialas

export async function predecir(entrada: Entrada): Promise<Prediccion> {
  // Simula la espera de la red (0.8 s)
  await new Promise((r) => setTimeout(r, 800));

  const i = Math.floor(Math.random() * ETIQUETAS.length);
  return {
    etiqueta: ETIQUETAS[i],
    confianza: Number((0.6 + Math.random() * 0.4).toFixed(2)),
  };
}