import { FlatList, StyleSheet, Text } from "react-native";
import { useHistorialViewModel } from "@/viewmodels/useHistorialViewModel";
import TarjetaResultado from "@/views/components/TarjetaResultado";

export default function HistorialScreen() {
  const vm = useHistorialViewModel();

  if (vm.vacio) {
    return <Text style={styles.vacio}>Aún no hay predicciones</Text>;
  }

  return (
    <FlatList
      data={vm.registros}
      keyExtractor={(r) => r.id}
      renderItem={({ item }) => (
        <TarjetaResultado prediccion={item} fecha={item.fecha} />
      )}
      contentContainerStyle={styles.lista}
    />
  );
}

const styles = StyleSheet.create({
  lista: { padding: 16, gap: 12 },
  vacio: { margin: 24, fontSize: 16, color: "#5A6170" },
});