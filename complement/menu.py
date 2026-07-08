import os

def menu_principal():
    print("1. SOLICITUDES")
    print("2. DATOS")
    print("3. SALIR")


def menu_solicitudes():
    print("1. AGREGAR USUARIO")
    print("2. BORRAR USUARIO")
    print("3. RESERVAR LIBRO")
    print("4. DEVOLVER LIBRO")
    print("5. VOLVER")


def menu_datos():
    print("1. USUARIOS REGISTRADOS")
    print("2. LIBROS")
    print("3. PRESTAMOS")
    print("4. VOLVER")


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')