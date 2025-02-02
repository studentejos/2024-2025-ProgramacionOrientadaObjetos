class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto(producto.get_id()) is None:
            self.productos.append(producto)
            print("Producto agregado.")
        else:
            print("Error: ID de producto ya existe.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.buscar_producto(id_producto)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)
