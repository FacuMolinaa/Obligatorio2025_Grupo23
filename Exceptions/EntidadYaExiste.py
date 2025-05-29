class EntidadYaExiste(Exception):
    def __init__ (self, mensaje = "La entidad ya existe."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)