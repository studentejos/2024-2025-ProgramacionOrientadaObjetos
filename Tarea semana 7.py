# Clase para gestionar una conexión a un archivo
class GestorArchivo:
    def __init__(self, nombre_archivo):
        """
        Constructor: Inicializa la clase y abre un archivo para escritura.
        :param nombre_archivo: Nombre del archivo a manejar.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        :param texto: Texto a escribir en el archivo.
        """
        self.archivo.write(texto + '\n')
        print(f"Texto escrito en el archivo '{self.nombre_archivo}'.")
