import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_LIBROS = os.path.join(BASE_DIR, "data", "libros.txt")


def mostrar_todos_los_libros():
    print("\n--- LISTADO GENERAL DE LIBROS ---")
    if not os.path.exists(RUTA_LIBROS):
        print("No hay archivo de libros todavia.")
        return

    contador = 0
    disponibles = 0
    with open(RUTA_LIBROS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) < 5:
                continue
            # partes[0]: ID, partes[1]: Titulo, partes[2]: Autor, partes[3]: Genero, partes[4]: Estado
            print(f"Nº: {partes[0]} - {partes[1]} por {partes[2]} ({partes[3]}) [{partes[4]}]")
            contador += 1
            if partes[4] == "ACTIVO":
                disponibles += 1
    print(f"\nTotal de libros: {contador} | Disponibles: {disponibles} | Reservados: {contador - disponibles}")