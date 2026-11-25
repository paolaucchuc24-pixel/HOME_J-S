import { useState } from "react";
import { CAMPOS } from "@/models/campos";
import { Entrada, Prediccion } from "@/models/Prediccion";
import { predecir } from "@/services/api";
import { guardar } from "@/services/historial";

// Un texto vacío por cada campo de CAMPOS
const VACIO: Record<string, string> = Object.fromEntries(
  CAMPOS.map((c) => [c.clave, ""])
);

export function usePrediccionViewModel() {
  const [campos, setCampos] = useState(VACIO);
  const [resultado, setResultado] =
    useState<Prediccion | null>(null);
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const actualizar = (clave: string, valor: string) =>
    setCampos({ ...campos, [clave]: valor });

  async function enviar() {
    const falta = CAMPOS.find((c) => campos[c.clave].trim() === "");
    if (falta) {
      setError(`Falta: ${falta.etiqueta}`);
      return;
    }
    setCargando(true);
    setError(null);
    try {
      const entrada: Entrada = Object.fromEntries(
        CAMPOS.map((c) => [c.clave, c.tipo === "numero"
          ? Number(campos[c.clave]) : campos[c.clave]])
      );
      const r = await predecir(entrada);
      setResultado(r);
      guardar(r);
    } catch {
      setError("No se pudo obtener la predicción");
    } finally {
      setCargando(false);
    }
  }
  return { campos, resultado, cargando, error, actualizar, enviar };
}