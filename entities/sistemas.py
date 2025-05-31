class Sistema:
    def __init__(self):
        self.clientes = []
        self.piezas = []
        self.maquinas = []
        self.ordenes = []
    
    def registrar_cliente(self, cliente):
        if cliente in self.clientes:
            raise ValueError("El cliente ya está registrado.")
        self.clientes.append(cliente)
        return cliente
    def registrar_pieza(self, pieza):
        if pieza in self.piezas:
            raise ValueError("La pieza ya está registrada.")
        self.piezas.append(pieza)
        return pieza
    def registrar_maquina(self, maquina):
        if maquina in self.maquinas:
            raise ValueError("La máquina ya está registrada.")
        self.maquinas.append(maquina)
        return maquina
    def registrar_orden(self, orden):
        if orden in self.ordenes:
            raise ValueError("La orden ya está registrada.")
        self.ordenes.append(orden)
        return orden
    def listar_clientes(self):
        return self.clientes
    def listar_piezas(self):
        if not self.piezas:
            raise ValueError("No hay piezas registradas.")
        return self.piezas
    def listar_maquinas(self):
        return self.maquinas
    def listar_ordenes(self):
        return self.ordenes
    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        raise ValueError("Cliente no encontrado.")
    def buscar_pieza(self, id_pieza):
        for pieza in self.piezas:
            if pieza.id_pieza == id_pieza:
                return pieza
        raise ValueError("Pieza no encontrada.")
    def buscar_maquina(self, id_maquina):
        for maquina in self.maquinas:
            if maquina.id_maquina == id_maquina:
                return maquina
        raise ValueError("Máquina no encontrada.")
    def buscar_orden(self, id_orden):
        for orden in self.ordenes:
            if orden.id_orden == id_orden:
                return orden
        raise ValueError("Orden no encontrada.")

    
    

    
     