
# Función para calcular el área de un rectángulo
def calcular_area(base: float, altura: float) -> float:
    return base * altura


# Función principal
def main():
    print("Cálculo de área de un rectángulo")

    # Entrada de datos
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    # Cálculo del área
    area = calcular_area(base, altura)

    # Mostrar resultado
    print(f"El área del rectángulo es: {area:.2f} unidades cuadradas")

    # Uso de diferentes tipos de datos
    nombre_usuario = "Estudiante"
    edad = 20
    es_estudiante = True

    print(f"Nombre: {nombre_usuario}, Edad: {edad}, Es estudiante: {es_estudiante}")


# Ejecutar el programa
if __name__ == "__main__":
    main()