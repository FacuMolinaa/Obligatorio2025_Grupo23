class Cliente:
    def __init__(self, nombre, direccion, telefono, correo):
        cliente = []
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class ClienteParticular(Cliente):
    def __init__(self, id_cliente, nombre, direccion, telefono, dni, correo):
        super().__init__(id_cliente, nombre, direccion, telefono, correo)
        self.id_cliente = id_cliente
        self.dni = dni

class ClienteEmpresa(Cliente):
    def __init__(self,id_cliente, nombre, direccion, telefono, correo):
        super().__init__(id_cliente, nombre, telefono, direccion, telefono, correo)
        self.id_cliente = id_cliente