class ExceptionPiezaYaExiste(Exception):
    def __init__(self, mensaje="La pieza ya existe."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)