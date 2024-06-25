import libros
import socios
import prestamos
import busquedadelibros
import generaciondereportes

def menu_principal():
    while True:
        print("=== Sistema de Gestión de Bibliotecas ===")
        print("1) Registro de libros")
        print("2) Gestión de socios")
        print("3) Registro de préstamos y devoluciones")
        print("4) Búsqueda de libros")
        print("5) Generación de reportes de préstamos y devoluciones")
        print("6) Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            libros.menu_libros()
        elif opcion == '2':
            socios.menu_socios()
        elif opcion == '3':
            prestamos.menu_prestamos()
        elif opcion == '4':
            busquedadelibros.buscar_libros()
        elif opcion == '5':
            generaciondereportes.generar_reportes()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
