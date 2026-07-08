import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_PRESTAMOS = os.path.join(BASE_DIR, "data", "prestamos.txt")
PRECIO_POR_DIA = 500


def mostrar_estadisticas():
    print("\n--- ESTADISTICAS DE LA BIBLIOTECA ---")

    if not os.path.exists(RUTA_PRESTAMOS):
        print("No hay datos de prestamos todavia.")
        return

    total_prestamos = 0
    prestamos_activos = 0
    prestamos_devueltos = 0
    total_multas = 0
    contador_libros = {}  # isbn -> { titulo, cantidad }

    with open(RUTA_PRESTAMOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue
            partes = linea_limpia.split(",")
            # Formato: [0]=DNI, [1]=nombre, [2]=titulo, [3]=isbn, [4]=dias, [5]=estado, [6]=monto(opt)
            if len(partes) < 6:
                continue

            isbn = partes[3]
            titulo = partes[2]
            estado = partes[5]

            # Contador general
            total_prestamos += 1

            # Contadores por estado
            if estado == "(RESERVADO)":
                prestamos_activos += 1
            elif estado == "(REINTEGRADO)":
                prestamos_devueltos += 1

            # Acumulador de multas
            if estado == "(REINTEGRADO)" and len(partes) > 6:
                try:
                    dias = int(partes[4])
                    monto_total = int(partes[6])
                    costo_base = dias * PRECIO_POR_DIA
                    multa = monto_total - costo_base
                    if multa > 0:
                        total_multas += multa
                except ValueError:
                    pass

            # Contador por libro
            if isbn not in contador_libros:
                contador_libros[isbn] = {"titulo": titulo, "cantidad": 0}
            contador_libros[isbn]["cantidad"] += 1

    if total_prestamos == 0:
        print("No hay prestamos registrados para mostrar estadisticas.")
        return

    # Mostrar totales
    print(f"\nTotal de prestamos registrados : {total_prestamos}")
    print(f"  - En curso (RESERVADO)       : {prestamos_activos}")
    print(f"  - Devueltos (REINTEGRADO)    : {prestamos_devueltos}")
    print(f"\nTotal de multas recaudadas     : ${total_multas}")

    # Ranking de libros mas solicitados
    if contador_libros:
        libros_ordenados = sorted(
            contador_libros.items(),
            key=lambda x: x[1]["cantidad"],
            reverse=True
        )

        print("\nRanking de libros mas solicitados:")
        for idx, (isbn, datos) in enumerate(libros_ordenados, 1):
            print(f"  {idx}. {datos['titulo']} (ISBN: {isbn}) — {datos['cantidad']} prestamo(s)")

        libro_top = libros_ordenados[0]
        print(f"\nLibro mas solicitado: '{libro_top[1]['titulo']}' con {libro_top[1]['cantidad']} prestamo(s).")
