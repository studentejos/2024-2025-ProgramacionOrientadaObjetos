# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad

    def presentarse(self):
        """Método para presentarse."""
        return f"Hola, me llamo {self._nombre} y tengo {self._edad} años."

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self._carrera = carrera

    # Sobrescribiendo el método para demostrar polimorfismo
    def presentarse(self):
        base = super().presentarse()  # Reutilizando el método de la clase base
        return f"{base} Soy estudiante de {self._carrera}."

# Otra clase derivada
class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self._especialidad = especialidad

    # Otro ejemplo de polimorfismo
    def presentarse(self):
        base = super().presentarse()
        return f"{base} Soy profesor especializado en {self._especialidad}."

# Clase adicional para encapsulación avanzada
class Notas:
    def __init__(self):
        self.__notas = []  # Atributo privado (doble subrayado)

    def agregar_nota(self, nota):
        """Agrega una nota validando que esté en el rango de 0 a 10."""
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida. Debe estar entre 0 y 10.")

    def promedio(self):
        """Calcula el promedio de las notas."""
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0

# Programa principal
def main():
    # Herencia y Polimorfismo
    persona = Persona("Carlos", 40)
    estudiante = Estudiante("Ana", 20, "Ingeniería")
    profesor = Profesor("Luis", 50, "Matemáticas")

    print(persona.presentarse())
    print(estudiante.presentarse())
    print(profesor.presentarse())

    # Encapsulación
    notas = Notas()
    notas.agregar_nota(8)
    notas.agregar_nota(9.5)
    notas.agregar_nota(11)  # Nota inválida
    print(f"Promedio de notas: {notas.promedio():.2f}")

