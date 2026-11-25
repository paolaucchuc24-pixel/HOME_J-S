import { StyleSheet, Text, TextInput, View } from "react-native";

type Props = {
  etiqueta: string;
  valor: string;
  tipo: "numero" | "texto";
  alCambiar: (texto: string) => void;
};

export default function CampoEntrada({ etiqueta, valor, tipo, alCambiar }: Props) {
  return (
    <View style={styles.caja}>
      <Text style={styles.etiqueta}>{etiqueta}</Text>
      <TextInput style={styles.input} value={valor} onChangeText={alCambiar}
        keyboardType={tipo === "numero" ? "numeric" : "default"}
        multiline={tipo === "texto"} />
    </View>
  );
}

const styles = StyleSheet.create({
  caja: { marginBottom: 12 },
  etiqueta: { fontSize: 14, color: "#5A6170", marginBottom: 4 },
  input: { borderWidth: 1, borderColor: "#D9DCE3",
           borderRadius: 8, padding: 10, fontSize: 16 },
});