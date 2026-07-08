from complement.menu import menu_principal, menu_solicitudes, menu_datos, limpiar_pantalla
from complement.usuarios import agregar_usuario, borrar_usuario, mostrar_todos_los_usuarios
from complement.prestamos import agregar_prestamo, agregar_devolucion, mostrar_todos_los_prestamos
from complement.libros import mostrar_todos_los_libros
from complement.estadisticas import mostrar_estadisticas

def main():
    while True:
        limpiar_pantalla()
        menu_principal()
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            while True:
                limpiar_pantalla()
                menu_solicitudes()
                sub_opcion = input("Ingrese una opción de Solicitudes: ").strip()

                if sub_opcion == "1":
                    agregar_usuario()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "2":
                    borrar_usuario()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "3":
                    agregar_prestamo()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "4":
                    agregar_devolucion()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "5":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción incorrecta.")
                    input("\nPresione Enter para continuar...") # <-- Agregado para pausar

        elif opcion == "2":
            while True:
                limpiar_pantalla()
                menu_datos()
                sub_opcion = input("Ingrese una opción de Datos: ").strip()
        
                if sub_opcion == "1":
                    mostrar_todos_los_usuarios()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "2":
                    mostrar_todos_los_libros()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "3":
                    mostrar_todos_los_prestamos()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "4":
                    mostrar_estadisticas()
                    input("\nPresione Enter para continuar...")
                elif sub_opcion == "5":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción incorrecta.")
                    input("\nPresione Enter para continuar...") # <-- Agregado para pausar

        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción ingresada incorrecta.")
            input("\nPresione Enter para continuar...")



if __name__ == "__main__":
    main()