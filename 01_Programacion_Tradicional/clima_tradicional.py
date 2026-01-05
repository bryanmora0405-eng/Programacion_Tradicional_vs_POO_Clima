# Programación Tradicional: Estructura de funciones

def ingresar_temperaturas():
    # Definimos una lista con las temperaturas diarias
    temperaturas = [22.5, 24.0, 21.0, 25.5, 23.0, 20.0, 22.0]
    return temperaturas

def calcular_promedio(temperaturas):
    # Lógica para calcular el promedio semanal
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Flujo principal
datos = ingresar_temperaturas()
resultado = calcular_promedio(datos)

print(f"Promedio semanal de temperaturas (Tradicional): {resultado:.2f}")
