import json

libros = []
current_id = 1

def cargar_libros():
    global libros, current_id
    try:
        with open("libros.json", "r") as file:
            libros = json.load(file)
        if libros:
            current_id = max(libro["id_libro"] for libro in libros) + 1
    except FileNotFoundError:
        libros = []

def guardar_libros():
    with open("libros.json", "w") as file:
        json.dump(libros, file, indent=4)

def registrar_libro():
    global current_id
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    ano_publicacion = input("Ingrese el año de publicación del libro: ")
    genero = input("Ingrese el género del libro: ")
    cantidad_disponible = int(input("Ingrese la cantidad disponible del libro: "))
    libro = {
        'id_libro': current_id,
        'titulo': titulo,
        'autor': autor,
        'editorial': editorial,
        'ano_publicacion': ano_publicacion,
        'genero': genero,
        'cantidad_disponible': cantidad_disponible
    }
    libros.append(libro)
    current_id += 1
    guardar_libros()
    print("Libro registrado exitosamente.")

def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
    else:
        for libro in libros:
            print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['ano_publicacion']}, Género: {libro['genero']}, Cantidad Disponible: {libro['cantidad_disponible']}")

def editar_libro():
    id_libro = int(input("Ingrese el ID del libro que desea editar: "))
    for libro in libros:
        if libro['id_libro'] == id_libro:
            libro['titulo'] = input(f"Ingrese el nuevo título del libro (anterior: {libro['titulo']}): ")
            libro['autor'] = input(f"Ingrese el nuevo autor del libro (anterior: {libro['autor']}): ")
            libro['editorial'] = input(f"Ingrese la nueva editorial del libro (anterior: {libro['editorial']}): ")
            libro['ano_publicacion'] = input(f"Ingrese el nuevo año de publicación del libro (anterior: {libro['ano_publicacion']}): ")
            libro['genero'] = input(f"Ingrese el nuevo género del libro (anterior: {libro['genero']}): ")
            libro['cantidad_disponible'] = int(input(f"Ingrese la nueva cantidad disponible del libro (anterior: {libro['cantidad_disponible']}): "))
            guardar_libros()
            print("Libro editado exitosamente.")
            return
    print("Libro no encontrado.")

def eliminar_libro():
    id_libro = int(input("Ingrese el ID del libro que desea eliminar: "))
    for libro in libros:
        if libro['id_libro'] == id_libro:
            libros.remove(libro)
            guardar_libros()
            print("Libro eliminado exitosamente.")
            return
    print("Libro no encontrado.")

def menu_libros():
    cargar_libros()  # Asegúrate de cargar los libros antes de mostrar el menú
    while True:
        print("=== Gestión de Libros ===")
        print("1) Registrar libro")
        print("2) Mostrar libros")
        print("3) Editar libro")
        print("4) Eliminar libro")
        print("5) Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_libro()
        elif opcion == '2':
            mostrar_libros()
        elif opcion == '3':
            editar_libro()
        elif opcion == '4':
            eliminar_libro()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
