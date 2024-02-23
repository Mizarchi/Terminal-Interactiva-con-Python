from registro_financiero import RegistroFinanciero
from transaccion import Transaccion
from datetime import datetime

def validar_fecha(fecha_texto):
    try:
        return datetime.strptime(fecha_texto, "%Y-%m-%d"), True
    except ValueError:
        print("Formato de fecha inválido. Por favor, use el formato YYYY-MM-DD.")
        return None, False

def solicitar_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            return monto
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def solicitar_fecha():
    while True:
        fecha_texto = input("Ingrese la fecha (YYYY-MM-DD): ")
        fecha, valido = validar_fecha(fecha_texto)
        if valido:
            return fecha_texto

def menu():
    registro = RegistroFinanciero()

    while True:
        print("\nMenú:")
        print("1. Registrar ingreso")
        print("2. Registrar gasto")
        print("3. Listar transacciones")
        print("4. Mostrar balance")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2']:
            monto = solicitar_monto()
            fecha = solicitar_fecha()
            descripcion = input("Ingrese la descripción: ")
            tipo = 'Ingreso' if opcion == '1' else 'Gasto'
            transaccion = Transaccion(monto, fecha, descripcion, tipo)
            registro.agregar_transaccion(transaccion)
        elif opcion == '3':
            registro.listar_transacciones()
        elif opcion == '4':
            registro.balance()
        elif opcion == '5':
            registro.guardar_datos()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
