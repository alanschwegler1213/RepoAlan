def main():
    # Título Principal
    print("¡Bienvenido al sistema de inscripción de la universidad!")

    # Datos Personales
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

    # Variable de Título Secundario
    tiene_titulo_secundario = True  # Puedes cambiar este valor según sea necesario

    # Monto de Matrícula y Cálculo de Cuota
    monto_matricula = float(input("Ingrese el monto de matrícula: "))
    cuota = monto_matricula + 1000

    # Arancel Especial para la Materia "Python I"
    arancel_python_i = 12000
    costo_mensual = arancel_python_i / 4  # Suponiendo que es un curso cuatrimestral

    # Pago en Efectivo
    pago_efectivo = input("¿El pago es en efectivo? (sí/no): ").strip().lower()
    if pago_efectivo == 'sí':
        descuento = 0.15
    else:
        descuento = 0.0
    
    cuota_final = cuota - (cuota * descuento)
    
    # Imprimir Datos
    print("\n--- Datos del Alumno ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Fecha de Nacimiento: {fecha_nacimiento}")
    print(f"Tiene Título Secundario: {'Sí' if tiene_titulo_secundario else 'No'}")
    print(f"Monto de Matrícula: ${monto_matricula:.2f}")
    print(f"Cuota (incluyendo $1000): ${cuota:.2f}")
    print(f"Arancel Especial 'Python I': ${arancel_python_i:.2f}")
    print(f"Costo Mensual de 'Python I': ${costo_mensual:.2f}")
    print(f"Cuota Final con Descuento (si corresponde): ${cuota_final:.2f}")

if __name__ == "__main__":
    main()
