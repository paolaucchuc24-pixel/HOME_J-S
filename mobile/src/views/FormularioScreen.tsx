import { ActivityIndicator, Pressable, ScrollView,
         StyleSheet, Text } from "react-native";
import { Link } from "expo-router";
import { CAMPOS } from "@/models/campos";
import { usePrediccionViewModel } from "@/viewmodels/usePrediccionViewModel";
import CampoEntrada from "@/views/components/CampoEntrada";
import TarjetaResultado from "@/views/components/TarjetaResultado";

export default function FormularioScreen() {
  const vm = usePrediccionViewModel();
  return (
    <ScrollView contentContainerStyle={styles.contenedor}>
      {CAMPOS.map((c) => (
        <CampoEntrada key={c.clave} etiqueta={c.etiqueta} tipo={c.tipo}
          valor={vm.campos[c.clave]}
          alCambiar={(t) => vm.actualizar(c.clave, t)} />
      ))}
      <Pressable style={styles.boton} onPress={vm.enviar} disabled={vm.cargando}>
        <Text style={styles.textoBoton}>Predecir</Text>
      </Pressable>
      {vm.cargando && <ActivityIndicator size="large" />}
      {vm.error && <Text style={styles.error}>{vm.error}</Text>}
      {vm.resultado && <TarjetaResultado prediccion={vm.resultado} />}
      <Link href="/historial" style={styles.link}>Ver historial</Link>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  contenedor: { padding: 20, gap: 8 },
  boton: { backgroundColor: "#14284B", padding: 14,
           borderRadius: 10, alignItems: "center" },
  textoBoton: { color: "#FFFFFF", fontWeight: "bold", fontSize: 16 },
  error: { color: "#B0413E" },
  link: { color: "#B8923A", textAlign: "center", marginTop: 12 },
});