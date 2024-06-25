import json
import datetime

prestamos = []
current_prestamo_id = 1

def cargar_prestamos():
    global prestamos, current_prestamo_id
    try:
        with open("prestamos.json", "r") as file:
            prestamos = json.load(file)
        if prestamos:
            current_prestamo_id = max(prestamo["id_prestamo"] for prestamo in prestamos) + 1
            for prestamo in prestamos:
                prestamo['fecha_prestamo'] = datetime.datetime.strptime(prestamo['fecha_prestamo'], "%Y-%m-%d")
                if prestamo['fecha_devolucion']:
                    prestamo['fecha_devolucion'] = datetime.datetime.strptime(prestamo['fecha_devolucion'], "%Y-%m-%d")
                if 'costo' not in prestamo:
                    prestamo['costo'] = 0.0  # Default value for costo if not present
    except FileNotFoundError:
        prestamos = []

def guardar_prestamos():
    with open("prestamos.json", "w") as file:
        prestamos_copy = []
        for prestamo in prestamos:
            prestamo_copy = prestamo.copy()
            prestamo_copy['fecha_prestamo'] = prestamo['fecha_prestamo'].strftime("%Y-%m-%d")
            if prestamo_copy['fecha_devolucion']:
                prestamo_copy['fecha_devolucion'] = prestamo_copy['fecha_devolucion'].strftime("%Y-%m-%d")
            prestamos_copy.append(prestamo_copy)
        json.dump(prestamos_copy, file, indent=4)

def registrar_prestamo():
    global current_prestamo_id
    id_socio = int(input("Ingrese el ID del socio: "))
    id_libro = int(input("Ingrese el ID del libro: "))
    
    while True:
        fecha_prestamo = input("Ingrese la fecha de préstamo (DD/MM/AAAA): ")
        try:
            fecha_prestamo = datetime.datetime.strptime(fecha_prestamo, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
    
    costo = float(input("Ingrese el costo del préstamo (si no tiene, ingrese 0): "))
    estado = "En Curso"
    
    prestamo = {
        'id_prestamo': current_prestamo_id,
        'id_socio': id_socio,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'costo': costo,
        'fecha_devolucion': None,
        'estado_prestamo': estado
    }
    
    prestamos.append(prestamo)
    current_prestamo_id += 1
    guardar_prestamos()
    print("Préstamo registrado exitosamente.")

def registrar_devolucion():
    id_prestamo = int(input("Ingrese el ID del préstamo que desea registrar la devolución: "))
    
    for prestamo in prestamos:
        if prestamo['id_prestamo'] == id_prestamo:
            while True:
                fecha_devolucion = input("Ingrese la fecha de devolución (DD/MM/AAAA): ")
                try:
                    fecha_devolucion = datetime.datetime.strptime(fecha_devolucion, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Fecha inválida. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
            
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo['estado_prestamo'] = "Devuelto"
            guardar_prestamos()
            print("Devolución registrada exitosamente.")
            return
    
    print("Préstamo no encontrado.")

def mostrar_prestamos():
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for prestamo in prestamos:
            fecha_prestamo = prestamo['fecha_prestamo'].strftime("%d/%m/%Y")
            fecha_devolucion = prestamo['fecha_devolucion'].strftime("%d/%m/%Y") if prestamo['fecha_devolucion'] else "N/A"
            print(f"ID: {prestamo['id_prestamo']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha de Préstamo: {fecha_prestamo}, Costo: {prestamo['costo']}, Fecha de Devolución: {fecha_devolucion}, Estado: {prestamo['estado_prestamo']}")

def menu_prestamos():
    cargar_prestamos()  # Cargar préstamos antes de mostrar el menú
    while True:
        print("=== Registro de Préstamos y Devoluciones ===")
        print("1) Registrar préstamo")
        print("2) Registrar devolución")
        print("3) Mostrar préstamos")
        print("4) Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_prestamo()
        elif opcion == '2':
            registrar_devolucion()
        elif opcion == '3':
            mostrar_prestamos()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
