import os
RUTA_USUARIOS = "data/usuarios.txt"
RUTA_PRESTAMOS = "data/prestamos.txt"


def agregar_usuario():
    print("\n--- AGREGAR NUEVO USUARIO ---")
    dni = input("Ingrese el DNI: ").strip()

    if dni == "":
        print("El DNI no puede estar vacio.")
        return

    # Comprobamos si el DNI ya esta en el archivo
    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if partes[0] == dni:
                    if partes[2] == "ACTIVO":
                        print("Este usuario ya existe y esta activo.")
                        return
                    elif partes[2] == "BAJA":
                        print("Este usuario existia pero estaba de baja.")
                        option = input("¿Quiere volver a activarlo? (S/N): ").upper()
                        if option == "S":
                            # Si dice que si, lo activamos modificando el archivo
                            cambiar_estado(dni, "ACTIVO")
                            print("Usuario reactivado con exito.")
                        return

    nombre = input("Ingrese el nombre completo: ").strip().upper()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return
    
    # Guardamos el nuevo registro
    with open(RUTA_USUARIOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{dni},{nombre},ACTIVO\n")
    print(f"Usuario {nombre} guardado correctamente.")


def borrar_usuario():
    print("\n--- DAR DE BAJA USUARIO ---")
    dni_buscar = input("Ingrese el DNI a dar de baja: ").strip()

    # 1. Primero vemos si existe, si esta activo y guardamos su nombre para validar
    encontrado = False
    nombre_usuario = ""
    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if partes[0] == dni_buscar and partes[2] == "ACTIVO":
                    encontrado = True
                    nombre_usuario = partes[1] # Guardamos el nombre (Ej: "JUAN PEREZ")
                    break

    if encontrado == False:
        print("No se encontro el usuario o ya esta de baja.")
        return

    # 2. NUEVA VALIDACIÓN: Revisamos si el usuario tiene algun libro (RESERVADO)
    tiene_libros_pendientes = False
    if os.path.exists(RUTA_PRESTAMOS):
        with open(RUTA_PRESTAMOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes_prestamo = linea.strip().split(",")
                # partes_prestamo[0] es el Nombre y partes_prestamo[4] es el Estado
                if partes_prestamo[0] == nombre_usuario and partes_prestamo[4] == "(RESERVADO)":
                    tiene_libros_pendientes = True
                    break

    if tiene_libros_pendientes == True:
        print(f"No se puede dar de baja a {nombre_usuario} porque tiene un libro RESERVADO sin devolver.")
        return

    # 3. Si paso la validación y no tiene deudas, le cambiamos el estado a BAJA
    cambiar_estado(dni_buscar, "BAJA")
    print("El usuario fue dado de baja.")


def mostrar_todos_los_usuarios():
    print("\n--- LISTADO GENERAL DE USUARIOS ---")
    if not os.path.exists(RUTA_USUARIOS):
        print("No hay archivo de usuarios todavia.")
        return

    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            # partes[0] es DNI, partes[1] es Nombre, partes[2] es ESTADO
            print(f"DNI: {partes[0]} - Nombre: {partes[1]} [{partes[2]}]")


# Funcion comun para modificar el estado (Activo/Baja) reescribiendo el archivo
def cambiar_estado(dni_objetivo, nuevo_estado):
    lineas_nuevas = []

    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if partes[0] == dni_objetivo:
                # Armamos la linea modificada
                lineas_nuevas.append(f"{partes[0]},{partes[1]},{nuevo_estado}\n")
            else:
                lineas_nuevas.append(linea)
    with open(RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas_nuevas)