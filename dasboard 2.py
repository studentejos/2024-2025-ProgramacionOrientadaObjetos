import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '2': "UNIDAD 2/SEMANA 2/2.1 Operadores Aritmeticos,Lógicos y relacionales.2py"
        '3': "UNIDAD 3/SEMANA 3/3.1 Arreglos.3py"
        '4': "UNIDAD 4/SEMANA 4/4.1 funciones, colecciones y archivos.4py"
        '5'. "UNIDAD 5/SEMANA 5/5.1 Función para calcular el área de un rectángulo.5py"
        '6': "UNIDAD 6/SEMANA 6/6.1 Función para calcular el área de un rectángulo.6py" 
        '7': "UNIDAD 7/SEMANA 7/7.1 Clase para gestionar una conexión a un archivo.7PY"

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()