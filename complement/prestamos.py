import os
RUTA_PRESTAMOS = "data/prestamos.txt"
RUTA_USUARIOS = "data/usuarios.txt"
RUTA_LIBROS = "data/libros.txt"
PRECIO_POR_DIA = 500      
MULTA_POR_DIA = 1000      


def agregar_prestamo():
    print("\n--- REGISTRAR NUEVO PRESTAMO ---")
    dni = input("Ingrese el DNI del usuario: ").strip()

    # 1. Buscar el nombre del usuario por su DNI
    nombre_usuario = ""

    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = linea_limpia.split(",")
                if partes[0] == dni and partes[2] == "ACTIVO":
                    nombre_usuario = partes[1]
                    break

    if nombre_usuario == "":
        print("El usuario no existe o esta de baja.")
        return

    # 2. Recolectar y mostrar todos los libros ACTIVOS (Disponibles)
    libros_disponibles = []
    if os.path.exists(RUTA_LIBROS):
        with open(RUTA_LIBROS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = linea_limpia.split(",")
                if len(partes) >= 5 and partes[4] == "ACTIVO":
                    libros_disponibles.append(partes)

    if len(libros_disponibles) == 0:
        print("No hay libros disponibles para prestamo en este momento.")
        return

    print("\nLibros disponibles para prestar:")

    for idx, libro in enumerate(libros_disponibles, 1):
        print(f"[{idx}] ISBN: {libro[0]} - Titulo: {libro[1]} por {libro[2]} ({libro[3]})")

    print("\nOpciones de prestamo:")
    print("1. Prestar un solo libro")
    print("2. Prestar multiples libros de la lista")

    opcion = input("Seleccione una opcion (1 o 2): ").strip()
    
    libros_a_prestar = []

    if opcion == "1":
        seleccion = input("Ingrese el numero del libro a prestar: ").strip()

        if not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > len(libros_disponibles):
            print("Seleccion invalida.")
            return
        libros_a_prestar.append(libros_disponibles[int(seleccion) - 1])

    elif opcion == "2":
        print("Ingrese los numeros de los libros separados por comas (Ejemplo: 1,3,4):")
        selecciones = input("Numeros de libros: ").strip().split(",")

        for sel in selecciones:
            sel = sel.strip()
            if sel.isdigit() and 1 <= int(sel) <= len(libros_disponibles):
                libro_elegido = libros_disponibles[int(sel) - 1]
                if libro_elegido not in libros_a_prestar:
                    libros_a_prestar.append(libro_elegido)

        if len(libros_a_prestar) == 0:
            print("No se seleccionaron libros validos.")
            return
    else:
        print("Opcion invalida.")
        return

    # 3. Solicitar la cantidad de días para cada libro seleccionado
    print("\n--- DETALLE DE REGISTRO ---")
    lineas_nuevas_prestamos = []

    for libro in libros_a_prestar:
        isbn = libro[0]
        nombre_libro = libro[1]
        print(f"\n> Libro: {nombre_libro} (ISBN: {isbn})")
        dias = input("  ¿Por cuantos dias se presta?: ").strip()

        if dias == "" or not dias.isdigit():
            print(f"  Cantidad invalida. Se cancelo el prestamo del libro: {nombre_libro}")
            continue

        # Cambiar el estado del libro a RESERVADO en libros.txt
        cambiar_estado_libro(isbn, "RESERVADO")

        # Preparar la línea para el archivo de préstamos
        nueva_linea = f"{nombre_usuario},{nombre_libro},{isbn},{dias},(RESERVADO)\n"
        lineas_nuevas_prestamos.append(nueva_linea)

    # 4. Guardar los nuevos préstamos en prestamos.txt
    if len(lineas_nuevas_prestamos) > 0:
        with open(RUTA_PRESTAMOS, "a", encoding="utf-8") as archivo:
            archivo.writelines(lineas_nuevas_prestamos)
        print("\nPrestamo(s) registrado(s) con exito. Los libros ahora figuran como RESERVADOS.")
    else:
        print("\nNo se pudo procesar ningun prestamo.")


def cambiar_estado_libro(isbn_objetivo, nuevo_estado):
    lineas_nuevas = []

    if os.path.exists(RUTA_LIBROS):
        with open(RUTA_LIBROS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = linea_limpia.split(",")
                if partes[0] == isbn_objetivo:
                    lineas_nuevas.append(f"{partes[0]},{partes[1]},{partes[2]},{partes[3]},{nuevo_estado}\n")
                else:
                    lineas_nuevas.append(linea_limpia + "\n")

        with open(RUTA_LIBROS, "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas_nuevas)