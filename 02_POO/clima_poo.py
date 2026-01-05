# Programación Orientada a Objetos: Uso de clases y objetos

class InformacionClima:
    def __init__(self, temperaturas):
        # Encapsulamos los datos dentro del objeto
        self.__temperaturas = temperaturas 

    def calcular_promedio_semanal(self):
        # El objeto sabe cómo calcular su propio promedio
        suma = sum(self.__temperaturas)
        return suma / len(self.__temperaturas)

# Uso del paradigma POO
mis_datos = [22.5, 24.0, 21.0, 25.5, 23.0, 20.0, 22.0]

# Creamos una instancia (objeto) de la clase
semana_actual = InformacionClima(mis_datos)

print(f"Promedio semanal de temperaturas (POO): {semana_actual.calcular_promedio_semanal():.2f}")
