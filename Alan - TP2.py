def mayor_unico(a, b, c):
    """
    Devuelve el mayor único de tres números positivos si existe, de lo contrario retorna -1.
    """
    # Comparar si 'a' es mayor estricto que 'b' y 'c'
    mayor_a = (a > b) * (a > c)
    
    # Comparar si 'b' es mayor estricto que 'a' y 'c'
    mayor_b = (b > a) * (b > c)
    
    # Comparar si 'c' es mayor estricto que 'a' y 'b'
    mayor_c = (c > a) * (c > b)
    
    # Sumar las comparaciones, si la suma es 1, significa que hay un mayor único
    resultado = mayor_a * a + mayor_b * b + mayor_c * c
    
    # Redondear el resultado al entero más cercano si es mayor a 0, o devolver -1 si no existe un mayor único
    return int(resultado) if resultado != 0 else -1

def main():
    # Solicitar al usuario los tres números positivos
    while True:
        try:
            a = float(input("Ingrese el primer número positivo: "))
            b = float(input("Ingrese el segundo número positivo: "))
            c = float(input("Ingrese el tercer número positivo: "))
            
            # Verificar que los números son positivos
            if a <= 0 or b <= 0 or c <= 0:
                print("Todos los números deben ser positivos. Intente de nuevo por favor.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

    # Llamar a la función mayor_unico
    resultado = mayor_unico(a, b, c)
    
    # Mostrar el resultado
    if resultado == -1:
        print("No existe un mayor único.")
    else:
        print(f"El mayor único es: {resultado}")

# Ejecutar el programa principal
main()

