def asignar_aula(dia):
    """Asignar el aula en función del número de día."""
    if dia % 2 == 0:
        return "A-300"
    else:
        return "A-315"

def imprimir_listado_aulas():
    """Imprimir el listado de días y aulas en formato de dos columnas."""
    print(f"{'Día':<5} {'Aula':<5}")  # Imprime los encabezados de las columnas
    
    for dia in range(1, 7):  # Itera sobre los números de días del 1 al 6
        aula = asignar_aula(dia)
        print(f"{dia:<5} {aula:<5}")  # Imprime el día y el aula en formato alineado

# Ejecutar la función para imprimir el listado
imprimir_listado_aulas()

