class Transaccion:
    def __init__(self, monto, fecha, descripcion, tipo):
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion
        self.tipo = tipo

    def __str__(self):
        return f"Fecha: {self.fecha}, {self.tipo}: ${self.monto}, Descripción: {self.descripcion}"
