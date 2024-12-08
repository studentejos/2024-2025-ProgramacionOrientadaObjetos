# Programación Orientada a Objetos - Ejemplo del Mundo Real

class Reserva:
    def __init__(self, cliente, fecha, num_personas):
        self.cliente = cliente
        self.fecha = fecha
        self.num_personas = num_personas

    def mostrar_reserva(self):
        return f"Reserva para {self.cliente} el {self.fecha} para {self.num_personas} personas."


class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        print("Reserva añadida con éxito.")

    def listar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
        else:
            for reserva in self.reservas:
                print(reserva.mostrar_reserva())