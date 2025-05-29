class Reposición:
    def __init__(self, pieza, cantidad, fecha):
        self.pieza = pieza
        self.cantidad = cantidad
        self.fecha = fecha
        self.fecha_reposición = None
    def registrar_reposición(self, fecha_reposición):
        if self.fecha_reposición is None:
            self.fecha_reposición = fecha_reposición
        else:
            raise ValueError("La reposición ya ha sido registrada.")