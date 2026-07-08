import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_PRESTAMOS = os.path.join(BASE_DIR, "data", "prestamos.txt")
RUTA_USUARIOS = os.path.join(BASE_DIR, "data", "usuarios.txt")
RUTA_LIBROS = os.path.join(BASE_DIR, "data", "libros.txt")
PRECIO_POR_DIA = 500
MULTA_POR_DIA = 1000


def agregar_prestamo():
    print("\n--- REGISTRAR NUEVO PRESTAMO ---")
    dni = input("Ingrese el DNI del usuario: ").strip()
    if not dni.isdigit():
        print("El DNI debe contener solo numeros.")
        return

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

        # Preparar la línea para el archivo de préstamos (incluye DNI)
        nueva_linea = f"{dni},{nombre_usuario},{nombre_libro},{isbn},{dias},(RESERVADO)\n"
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


def agregar_devolucion():
    print("\n--- REGISTRAR DEVOLUCION ---")
    dni_buscar = input("Ingrese el DNI del usuario: ").strip()
    if not dni_buscar.isdigit():
        print("El DNI debe contener solo numeros.")
        return

    # 1. Buscar el nombre del usuario usando el DNI
    nombre_buscar = ""

    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = linea_limpia.split(",")
                if partes[0] == dni_buscar:
                    nombre_buscar = partes[1]
                    break

    if nombre_buscar == "":
        print("No se encontro ningun usuario registrado con ese DNI.")
        return

    # 2. Recolectar todos los préstamos RESERVADOS de este usuario (busca por DNI)
    prestamos_activos = []
    if os.path.exists(RUTA_PRESTAMOS):
        with open(RUTA_PRESTAMOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = linea_limpia.split(",")
                # Formato: [0]=DNI, [1]=nombre, [2]=titulo, [3]=isbn, [4]=dias, [5]=estado
                if len(partes) >= 6 and partes[0] == dni_buscar and partes[5] == "(RESERVADO)":
                    prestamos_activos.append(partes)

    if len(prestamos_activos) == 0:
        print(f"El usuario {nombre_buscar} no tiene libros pendientes de devolucion.")
        return

    # 3. Mostrar los libros que tiene en su poder
    print(f"\nEl usuario {nombre_buscar} debe reintegrar los siguientes libros:")
    for idx, prestamo in enumerate(prestamos_activos, 1):
        # [3]=isbn, [2]=titulo, [4]=dias
        print(f"[{idx}] ISBN: {prestamo[3]} - Titulo: {prestamo[2]} (Dias pactados: {prestamo[4]})")

    print("\nOpciones de devolucion:")
    print("1. Reintegrar un solo libro (1 por 1)")
    print("2. Reintegrar TODOS los libros de una vez")
    opcion = input("Seleccione una opcion (1 o 2): ").strip()

    libros_a_devolver = []

    if opcion == "1":
        seleccion = input("Ingrese el numero del libro a devolver de la lista: ").strip()
        if not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > len(prestamos_activos):
            print("Seleccion invalida.")
            return
        libros_a_devolver.append(prestamos_activos[int(seleccion) - 1])
    elif opcion == "2":
        libros_a_devolver = prestamos_activos
    else:
        print("Opcion invalida.")
        return

    # 4. Procesar los cálculos individuales, tickets e importes finales
    isbns_devueltos = [p[3] for p in libros_a_devolver]  # isbn está en [3]
    tickets_calculados = {}

    print("\n--- DETALLE DE LIQUIDACION ---")
    for prestamo in libros_a_devolver:
        titulo_libro = prestamo[2]   # titulo en [2]
        isbn_libro = prestamo[3]     # isbn en [3]
        try:
            dias_pactados = int(prestamo[4])  # dias en [4]
        except ValueError:
            print(f"  Error al leer los dias del préstamo de '{titulo_libro}'. Se omite.")
            continue

        print(f"\n> Libro: {titulo_libro} (ISBN: {isbn_libro})")
        dias_reales_str = input(f"  El prestamo era por {dias_pactados} dias. ¿Cuantos dias pasaron en realidad?: ").strip()
        if dias_reales_str == "" or not dias_reales_str.isdigit():
            print("  Cantidad invalida. Se cancelo el proceso.")
            return

        dias_reales = int(dias_reales_str)
        costo_base = dias_pactados * PRECIO_POR_DIA
        dias_demora = 0
        multa = 0

        if dias_reales > dias_pactados:
            dias_demora = dias_reales - dias_pactados
            multa = dias_demora * MULTA_POR_DIA

        total_libro = costo_base + multa

        tickets_calculados[isbn_libro] = {
            'base': costo_base,
            'demora': dias_demora,
            'multa': multa,
            'total': total_libro,
            'titulo': titulo_libro
        }

    # 5. Reescribir el archivo prestamos.txt actualizando los estados
    lineas_nuevas_prestamos = []
    if os.path.exists(RUTA_PRESTAMOS):
        with open(RUTA_PRESTAMOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                partes = linea_limpia.split(",")

                # Formato: [0]=DNI, [1]=nombre, [2]=titulo, [3]=isbn, [4]=dias, [5]=estado
                if len(partes) >= 6:
                    if partes[0] == dni_buscar and partes[5] == "(RESERVADO)" and partes[3] in isbns_devueltos:
                        isbn_act = partes[3]
                        monto_final = tickets_calculados[isbn_act]['total']
                        linea = f"{partes[0]},{partes[1]},{partes[2]},{partes[3]},{partes[4]},(REINTEGRADO),{monto_final}\n"
                        cambiar_estado_libro(isbn_act, "ACTIVO")
                    else:
                        linea = linea_limpia + "\n"
                lineas_nuevas_prestamos.append(linea)

    with open(RUTA_PRESTAMOS, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas_nuevas_prestamos)

    # 6. Desplegar el Ticket definitivo consolidado
    print("\n========================================")
    print("         TICKET DE DEVOLUCION           ")
    print("========================================")
    print(f"DNI: {dni_buscar} - Usuario: {nombre_buscar}")
    total_general = 0

    for isbn, datos in tickets_calculados.items():
        print(f"\n* {datos['titulo']} ({isbn})")
        print(f"  - Costo base ({PRECIO_POR_DIA}/dia): ${datos['base']}")
        if datos['multa'] > 0:
            print(f"  - Dias de retraso: {datos['demora']} dias (Multa por dia: ${MULTA_POR_DIA})")
            print(f"  - Monto de multa: ${datos['multa']}")
        print(f"  - Total de este libro: ${datos['total']}")
        total_general += datos['total']

    print("\n========================================")
    print(f" TOTAL GENERAL A ABONAR: ${total_general}")
    print("========================================")
    print("Devolucion efectuada y registros actualizados correctamente.")


def mostrar_todos_los_prestamos():
    print("\n--- LISTADO GENERAL DE PRESTAMOS ---")
    if not os.path.exists(RUTA_PRESTAMOS):
        print("No hay archivo de prestamos todavia.")
        return

    with open(RUTA_PRESTAMOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue
            partes = linea_limpia.split(",")

            # Formato: [0]=DNI, [1]=nombre, [2]=titulo, [3]=isbn, [4]=dias, [5]=estado, [6]=monto(opt)
            if len(partes) >= 6:
                dni_u = partes[0]
                usuario = partes[1]
                libro = partes[2]
                isbn = partes[3]
                dias = partes[4]
                estado = partes[5]

                if estado == "(REINTEGRADO)":
                    if len(partes) > 6:
                        importe_abonado = partes[6]
                    else:
                        try:
                            importe_abonado = int(dias) * PRECIO_POR_DIA
                        except ValueError:
                            importe_abonado = "?"
                    print(f"DNI: {dni_u} - Usuario: {usuario} - Libro: {libro} (ISBN: {isbn}) - Dias: {dias} [{estado}] - Importe Abonado: ${importe_abonado}")
                else:
                    print(f"DNI: {dni_u} - Usuario: {usuario} - Libro: {libro} (ISBN: {isbn}) - Dias: {dias} [{estado}]")