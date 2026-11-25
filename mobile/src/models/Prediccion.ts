// Cómo se captura cada dato en pantalla
export type Campo = {
  clave: string;      // nombre que espera el modelo
  etiqueta: string;   // texto que ve el usuario
  tipo: "numero" | "texto";
};

// Lo que se envía al modelo: { clave: valor }
export type Entrada = Record<string, number | string>;

// Lo que regresa la predicción
export type Prediccion = {
  etiqueta: string;   // clase o valor predicho
  confianza: number;  // de 0 a 1
};

// Una predicción guardada en el historial
export type Registro = Prediccion & { id: string; fecha: string };