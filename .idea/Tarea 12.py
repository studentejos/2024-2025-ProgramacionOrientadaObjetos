class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {[libro.titulo for libro in self.libros_prestados]}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # ISBN -> Libro
        self.usuarios = {}  # ID Usuario -> Usuario

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("ISBN no encontrado en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El ID de usuario ya existe.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            print(f"Usuario dado de baja: {eliminado.nombre}")
        else:
            print("ID de usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("ID de usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio, "") == valor]
        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("ID de usuario no encontrado.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234")
libro2 = Libro("1984", "George Orwell", "Distopía", "5678")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("001", "1234")
biblioteca.listar_libros_prestados("001")
biblioteca.devolver_libro("001", "1234")
biblioteca.listar_libros_prestados("001")

# Buscar libros
biblioteca.buscar_libro("autor", "George Orwell")
