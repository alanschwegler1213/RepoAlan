def cargar_edades():
    """Solicitar edades válidas y contar cargas erróneas."""
    edades_erroneas = 0

    while True:
        try:
            edad = int(input("Ingrese la edad (mayor o igual a 18 para finalizar): "))
            if edad < 18:
                print("Edad inválida. Debe ser mayor de edad.")
                edades_erroneas += 1
            else:
                # Si la edad es válida, salimos del bucle
                break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    print(f"\nEdad ingresada: {edad}")
    print(f"Cantidad de cargas erróneas: {edades_erroneas}")
    print("\n")  # Línea separadora


def promedio_notas(rango_notas):
    """Cargar notas de alumnos y calcular el promedio."""
    total_notas = 0

    for i in range(rango_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
                if 0 <= nota <= 10:
                    total_notas += nota
                    break
                else:
                    print("Nota inválida. Debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número decimal.")

    promedio = total_notas / rango_notas
    print(f"Promedio de las notas: {promedio:.2f}")
    print("\n")  # Línea separadora


def costo_comedor():
    """Calcular el costo del comedor y mostrar el informe."""
    costo_por_dia = 1250

    print("\n")
    for dias in range(1, 7):  # Desde 1 hasta 6 días
        costo_total = dias * costo_por_dia
        print(f"{dias} día(s) cuesta ${costo_total}")
    print("\n")  # Línea separadora


# Ejecutar las funciones en el orden deseado
cargar_edades()
promedio_notas(5)
costo_comedor()
