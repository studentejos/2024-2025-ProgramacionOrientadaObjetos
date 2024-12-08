# Programación Tradicional

def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def main_tradicional():
    print("--- Promedio Semanal del Clima (Tradicional) ---")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


# Programación Orientada a Objetos

class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


def main_poo():
    print("--- Promedio Semanal del Clima (POO) ---")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


# Llamado a ambas versiones
if __name__ == "__main__":
    main_tradicional()
    print("\n")
    main_poo()
