import prestamos
import datetime

def generar_reportes():
    prestamos.cargar_prestamos()  # Cargar los préstamos antes de generar reportes
    while True:
        print("=== Generación de Reportes ===")
        print("1) Reporte por socio")
        print("2) Reporte por libro")
        print("3) Reporte por rango de fechas")
        print("4) Generar estadísticas")
        print("5) Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            reporte_por_socio()
        elif opcion == '2':
            reporte_por_libro()
        elif opcion == '3':
            reporte_por_rango_fechas()
        elif opcion == '4':
            generar_estadisticas()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def reporte_por_socio():
    id_socio = int(input("Ingrese el ID del socio: "))
    resultados = [prestamo for prestamo in prestamos.prestamos if prestamo['id_socio'] == id_socio]
    if resultados:
        for prestamo in resultados:
            mostrar_detalle_prestamo(prestamo)
    else:
        print(f"No se encontraron préstamos para el socio con ID: {id_socio}.")

def reporte_por_libro():
    id_libro = int(input("Ingrese el ID del libro: "))
    resultados = [prestamo for prestamo in prestamos.prestamos if prestamo['id_libro'] == id_libro]
    if resultados:
        for prestamo in resultados:
            mostrar_detalle_prestamo(prestamo)
    else:
        print(f"No se encontraron préstamos para el libro con ID: {id_libro}.")

def reporte_por_rango_fechas():
    while True:
        try:
            fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/AAAA): ")
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
            fecha_fin = input("Ingrese la fecha de fin (DD/MM/AAAA): ")
            fecha_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
    
    resultados = [prestamo for prestamo in prestamos.prestamos if fecha_inicio <= prestamo['fecha_prestamo'] <= fecha_fin]
    if resultados:
        for prestamo in resultados:
            mostrar_detalle_prestamo(prestamo)
    else:
        print(f"No se encontraron préstamos en el rango de fechas: {fecha_inicio.strftime('%d/%m/%Y')} - {fecha_fin.strftime('%d/%m/%Y')}.")

def mostrar_detalle_prestamo(prestamo):
    fecha_prestamo = prestamo['fecha_prestamo'].strftime("%d/%m/%Y")
    fecha_devolucion = prestamo['fecha_devolucion'].strftime("%d/%m/%Y") if prestamo['fecha_devolucion'] else "N/A"
    print(f"ID Préstamo: {prestamo['id_prestamo']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha de Préstamo: {fecha_prestamo}, Costo: {prestamo['costo']}, Fecha de Devolución: {fecha_devolucion}, Estado: {prestamo['estado_prestamo']}")

def generar_estadisticas():
    total_prestamos = len(prestamos.prestamos)
    prestamos_por_socio = {}
    prestamos_por_libro = {}

    for prestamo in prestamos.prestamos:
        id_socio = prestamo['id_socio']
        id_libro = prestamo['id_libro']

        if id_socio not in prestamos_por_socio:
            prestamos_por_socio[id_socio] = 0
        prestamos_por_socio[id_socio] += 1

        if id_libro not in prestamos_por_libro:
            prestamos_por_libro[id_libro] = 0
        prestamos_por_libro[id_libro] += 1

    socio_con_mas_prestamos = max(prestamos_por_socio, key=prestamos_por_socio.get)
    libro_mas_prestado = max(prestamos_por_libro, key=prestamos_por_libro.get)

    print("=== Estadísticas ===")
    print(f"Total de préstamos: {total_prestamos}")
    print(f"Socio con más préstamos: ID {socio_con_mas_prestamos} con {prestamos_por_socio[socio_con_mas_prestamos]} préstamos")
    print(f"Libro más prestado: ID {libro_mas_prestado} con {prestamos_por_libro[libro_mas_prestado]} préstamos")
