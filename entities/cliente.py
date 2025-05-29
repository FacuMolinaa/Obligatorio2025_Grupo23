class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class ClienteParticular:
    def __init__(self, id_cliente, nombre, direccion, telefono, dni):
        super().__init__(id_cliente, nombre, direccion, telefono)
        self.dni = dni

class ClienteEmpresa(Cliente):
    def __init__(self,id_cliente, dni, nombre, direccion, telefono):
        super().__init__(id_cliente, nombre, telefono, direccion, telefono)
        self.dni = dni
