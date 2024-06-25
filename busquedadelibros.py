import libros

def buscar_libros():
    while True:
        print("=== Búsqueda de Libros ===")
        print("1) Buscar por título")
        print("2) Buscar por género")
        print("3) Buscar por autor")
        print("4) Buscar por editorial")
        print("5) Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            buscar_por_campo("titulo")
        elif opcion == '2':
            buscar_por_campo("genero")
        elif opcion == '3':
            buscar_por_campo("autor")
        elif opcion == '4':
            buscar_por_campo("editorial")
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def buscar_por_campo(campo):
    valor = input(f"Ingrese el {campo} del libro que desea buscar: ").strip().lower()
    resultados = [libro for libro in libros.libros if libro[campo].strip().lower() == valor]
    if resultados:
        for libro in resultados:
            print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['ano_publicacion']}, Género: {libro['genero']}, Cantidad Disponible: {libro['cantidad_disponible']}")
    else:
        print(f"No se encontraron libros con {campo}: {valor}.")
