def asignar_aula(dia):
    """Asignar el aula en función del número de día."""
    if dia % 2 == 0:
        return "Aula: A-300"
    else:
        return "Aula: A-315"

def calcular_cuota_con_descuento(turno, num_materias, cuota):
    """Calcular el valor de la cuota con descuento basado en el turno y número de materias."""
    if turno == "tarde" and num_materias > 3:
        descuento = 0.25
    else:
        descuento = 0.05

    cuota_con_descuento = cuota * (1 - descuento)
    return cuota_con_descuento

def calcular_costo_estacionamiento(tipo_vehiculo):
    """Calcular el costo de estacionamiento basado en el tipo de vehículo."""
    tipo_vehiculo = tipo_vehiculo.lower()
    if tipo_vehiculo == "auto" or tipo_vehiculo == "moto":
        return 300
    elif tipo_vehiculo == "bicicleta":
        return 50
    else:
        return None  # Valor que indica un tipo de vehículo no válido.

def main():
    # Parte A: Asignación de Aula
    while True:
        try:
            dia = int(input("Ingrese el número de día (1-6): "))
            if dia < 1 or dia > 6:
                print("Número de día inválido. Debe ser entre 1 y 6.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    aula = asignar_aula(dia)
    print(aula)

    # Parte B: Cálculo de Descuento en la Cuota
    while True:
        turno = input("Ingrese el turno (mañana/tarde): ").strip().lower()
        if turno not in ["mañana", "tarde"]:
            print("Turno inválido. Debe ser 'mañana' o 'tarde'.")
        else:
            break

    while True:
        try:
            num_materias = int(input("Ingrese el número de materias: "))
            if num_materias < 0:
                print("Número de materias inválido. Debe ser un número entero no negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    while True:
        try:
            cuota = float(input("Ingrese el valor de la cuota: "))
            if cuota < 0:
                print("Valor de la cuota inválido. Debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número decimal.")

    cuota_con_descuento = calcular_cuota_con_descuento(turno, num_materias, cuota)
    print(f"Valor de la cuota con descuento: ${cuota_con_descuento:.2f}")

    # Parte C: Cálculo de Costo de Estacionamiento
    while True:
        tipo_vehiculo = input("Ingrese el tipo de vehículo (auto/moto/bicicleta): ").strip().lower()
        costo_estacionamiento = calcular_costo_estacionamiento(tipo_vehiculo)
        if costo_estacionamiento is None:
            print("Tipo de vehículo no válido. Debe ser 'auto', 'moto' o 'bicicleta'.")
        else:
            break

    print(f"Costo de estacionamiento: ${costo_estacionamiento}")

if __name__ == "__main__":
    main()

