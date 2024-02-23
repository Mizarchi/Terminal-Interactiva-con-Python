import pickle
from transaccion import Transaccion

class RegistroFinanciero:
    def __init__(self, archivo_datos='datos_financieros.pkl'):
        self.archivo_datos = archivo_datos
        self.transacciones = self.cargar_datos()

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)
        print("Transacción agregada correctamente.")

    def listar_transacciones(self):
        for transaccion in sorted(self.transacciones, key=lambda x: x.fecha):
            print(transaccion)

    def balance(self):
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'Ingreso')
        gastos = sum(t.monto for t in self.transacciones if t.tipo == 'Gasto')
        capacidad_ahorro = ingresos - gastos
        print(f"Total Ingresos: ${ingresos}, Total Gastos: ${gastos}, Capacidad de Ahorro: ${capacidad_ahorro}")

    def guardar_datos(self):
        with open(self.archivo_datos, 'wb') as archivo:
            pickle.dump(self.transacciones, archivo)
        print("Datos guardados exitosamente.")

    def cargar_datos(self):
        try:
            with open(self.archivo_datos, 'rb') as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            print("No se encontró el archivo. Iniciando con una lista de transacciones vacía.")
            return []
