def main():
    # Título Principal
    print("¡Bienvenido al sistema de inscripción de la universidad!")

    # Datos Personales
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

   # Notas de Exámenes
    nota1 = float(input("Ingrese la nota del primer examen: "))
    nota2 = float(input("Ingrese la nota del segundo examen: "))

    # Promedio
    promedio = (nota1 + nota2) / 2

    # Determinar el resultado del último examen
    if nota2 >= 7:
        resultado_examen = "Aprobó el último examen."
    else:
        resultado_examen = "Desaprobó el último examen."

    # Comparación de Desempeño
    if nota2 > nota1:
        desempeño = "Mejoró su desempeño."
    elif nota2 == nota1:
        desempeño = "Mantuvo la nota."
    else:
        desempeño = "Empeoró su desempeño."

    # Determinar el estado de la materia
    if promedio >= 7:
        estado_materia = "Promocionó la materia."
    elif promedio >= 4:
        estado_materia = "Debe rendir final."
    else:
        estado_materia = "Debe recursar."


    # Imprimir Datos
    print("\n--- Datos del Alumno ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Fecha de Nacimiento: {fecha_nacimiento}")
    print(f"Nota del Primer Examen: {nota1:.2f}")
    print(f"Nota del Segundo Examen: {nota2:.2f}")
    print(f"Promedio de Exámenes: {promedio:.2f}")
    print(f"Resultado del Último Examen: {resultado_examen}")
    print(f"Progreso del 1er al 2do parcial: {desempeño}")
    print(f"Estado: {(estado_materia)}")

if __name__ == "__main__":
    main()
