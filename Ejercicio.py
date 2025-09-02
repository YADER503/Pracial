# Sistema de registro de viajes en transporte público
def registrar_viajes():
	viajes = []
	print("Registro de viajes semanales (transporte público)")
	while True:
		ruta = input("Ruta (nombre o número): ")
		costo = float(input("Costo del viaje ($): "))
		tiempo = float(input("Tiempo del viaje (minutos): "))
		viajes.append({"ruta": ruta, "costo": costo, "tiempo": tiempo})
		otro = input("¿Registrar otro viaje? (s/n): ").lower()
		if otro != 's':
			break
	return viajes

def mostrar_viajes(viajes):
	print("\n--- Viajes realizados ---")
	viajes_ordenados = sorted(viajes, key=lambda x: x["costo"], reverse=True)
	for i, v in enumerate(viajes_ordenados, 1):
		print(f"{i}. Ruta: {v['ruta']}, Costo: ${v['costo']:.2f}, Tiempo: {v['tiempo']} min")

def resumen(viajes):
	total_gasto = sum(v["costo"] for v in viajes)
	total_tiempo = sum(v["tiempo"] for v in viajes)
	print("\n--- Resumen semanal ---")
	print(f"Gasto total: ${total_gasto:.2f}")
	print(f"Tiempo total invertido: {total_tiempo} minutos")

def main():
	viajes = registrar_viajes()
	mostrar_viajes(viajes)
	resumen(viajes)

if __name__ == "__main__":
	main()
