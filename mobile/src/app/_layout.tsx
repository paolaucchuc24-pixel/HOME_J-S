import { Stack } from "expo-router";

export default function Layout() {
  return (
    <Stack screenOptions={{
      headerStyle: { backgroundColor: "#14284B" },
      headerTintColor: "#FFFFFF",
    }}>
      <Stack.Screen name="index"
        options={{ title: "Nueva predicción" }} />
      <Stack.Screen name="historial"
        options={{ title: "Historial" }} />
    </Stack>
  );
}