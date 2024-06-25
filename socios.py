import json

socios = []
current_socio_id = 1

def cargar_socios():
    global socios, current_socio_id
    try:
        with open("socios.json", "r") as file:
            socios = json.load(file)
        if socios:
            current_socio_id = max(socio["id_socio"] for socio in socios) + 1
    except FileNotFoundError:
        socios = []

def guardar_socios():
    with open("socios.json", "w") as file:
        json.dump(socios, file, indent=4)

def registrar_socio():
    global current_socio_id
    nombre = input("Ingrese el nombre del socio: ")
    apellido = input("Ingrese el apellido del socio: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del socio (DD/MM/AAAA): ")
    direccion = input("Ingrese la dirección del socio: ")
    email = input("Ingrese el correo electrónico del socio: ")
    telefono = input("Ingrese el teléfono del socio: ")
    socio = {
        'id_socio': current_socio_id,
        'nombre': nombre,
        'apellido': apellido,
        'fecha_nacimiento': fecha_nacimiento,
        'direccion': direccion,
        'correo_electronico': email,
        'telefono': telefono
    }
    socios.append(socio)
    current_socio_id += 1
    guardar_socios()
    print("Socio registrado exitosamente.")

def mostrar_socios():
    if not socios:
        print("No hay socios registrados.")
    else:
        for socio in socios:
            print(f"ID: {socio['id_socio']}, Nombre: {socio['nombre']}, Apellido: {socio['apellido']}, Fecha de Nacimiento: {socio['fecha_nacimiento']}, Dirección: {socio['direccion']}, Email: {socio['correo_electronico']}, Teléfono: {socio['telefono']}")

def editar_socio():
    id_socio = int(input("Ingrese el ID del socio que desea editar: "))
    for socio in socios:
        if socio['id_socio'] == id_socio:
            socio['nombre'] = input(f"Ingrese el nuevo nombre del socio (anterior: {socio['nombre']}): ")
            socio['apellido'] = input(f"Ingrese el nuevo apellido del socio (anterior: {socio['apellido']}): ")
            socio['fecha_nacimiento'] = input(f"Ingrese la nueva fecha de nacimiento del socio (anterior: {socio['fecha_nacimiento']}): ")
            socio['direccion'] = input(f"Ingrese la nueva dirección del socio (anterior: {socio['direccion']}): ")
            socio['correo_electronico'] = input(f"Ingrese el nuevo correo electrónico del socio (anterior: {socio['correo_electronico']}): ")
            socio['telefono'] = input(f"Ingrese el nuevo teléfono del socio (anterior: {socio['telefono']}): ")
            guardar_socios()
            print("Socio editado exitosamente.")
            return
    print("Socio no encontrado.")

def eliminar_socio():
    id_socio = int(input("Ingrese el ID del socio que desea eliminar: "))
    for socio in socios:
        if socio['id_socio'] == id_socio:
            socios.remove(socio)
            guardar_socios()
            print("Socio eliminado exitosamente.")
            return
    print("Socio no encontrado.")

def menu_socios():
    cargar_socios()  # Asegúrate de cargar los socios antes de mostrar el menú
    while True:
        print("=== Gestión de Socios ===")
        print("1) Registrar socio")
        print("2) Mostrar socios")
        print("3) Editar socio")
        print("4) Eliminar socio")
        print("5) Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_socio()
        elif opcion == '2':
            mostrar_socios()
        elif opcion == '3':
            editar_socio()
        elif opcion == '4':
            eliminar_socio()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
