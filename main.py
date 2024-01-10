# Programa para calcular el área de un cuadrado

# Función para calcular el área del cuadrado
def calcular_area_cuadrado(base, altura):
    """
    Esta función toma la base y la altura de un cuadrado y devuelve el área.

    Parámetros:
    - base (float): La longitud de la base del cuadrado.
    - altura (float): La altura del cuadrado.

    Retorna:
    float: El área del cuadrado.
    """
    area = base * altura
    return area


# Entrada de datos desde el usuario
base_cuadrado = float(input("Ingrese la longitud de la base del cuadrado: "))
altura_cuadrado = float(input("Ingrese la altura del cuadrado: "))

# Llamada a la función para calcular el área
area_resultante = calcular_area_cuadrado(base_cuadrado, altura_cuadrado)

# Mostrar el resultado
print(f"El área del cuadrado con base {base_cuadrado} y altura {altura_cuadrado} es: {area_resultante}")