import { useCallback, useState } from "react";
import { useFocusEffect } from "expo-router";
import { Registro } from "@/models/Prediccion";
import { obtenerHistorial } from "@/services/historial";

export function useHistorialViewModel() {
  const [registros, setRegistros] = useState<Registro[]>([]);

  // Se ejecuta cada vez que la pantalla se muestra
  useFocusEffect(
    useCallback(() => {
      setRegistros(obtenerHistorial());
    }, [])
  );

  return { registros, vacio: registros.length === 0 };
}