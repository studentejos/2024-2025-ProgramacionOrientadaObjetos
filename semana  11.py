import pickle

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_cantidad(self, id, nueva_cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(nueva_cantidad)
        else:
            print("Producto no encontrado.")

    def actualizar_precio(self, id, nuevo_precio):
        if id in self.productos:
            self.productos[id].set_precio(nuevo_precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self.productos, archivo)

    def cargar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as archivo:
                self.productos = pickle.load(archivo)
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")




