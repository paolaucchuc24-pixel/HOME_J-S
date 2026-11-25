import { StyleSheet, Text, View } from "react-native";
import { Prediccion } from "@/models/Prediccion";

type Props = { prediccion: Prediccion; fecha?: string };

export default function TarjetaResultado({ prediccion, fecha }: Props) {
  return (
    <View style={styles.tarjeta}>
      <Text style={styles.etiqueta}>{prediccion.etiqueta}</Text>
      <Text>Confianza: {Math.round(prediccion.confianza * 100)} %</Text>
      {fecha && <Text style={styles.fecha}>{fecha}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  tarjeta: { backgroundColor: "#F3F5F9", borderRadius: 12, padding: 16 },
  etiqueta: { fontSize: 20, fontWeight: "bold", color: "#14284B" },
  fecha: { color: "#5A6170", marginTop: 4 },
});