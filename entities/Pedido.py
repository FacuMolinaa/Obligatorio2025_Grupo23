class Pedido:
    def _init__(self,cliente,maquina,pieza):
        self.cliente = cliente
        self.maquina = maquina
        self.pieza = pieza
        self.requerimientos = []
        self.estado = "Pendiente" 
        self.fecha_registro = None
        self.fecha_entrega = None
    def agregar_requerimiento(self, requerimiento):
        self.requerimientos.append(requerimiento)
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "En Proceso", "Completado", "Cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            raise ValueError(f"Estado inválido: {nuevo_estado}. Debe ser uno de {estados_validos}.")
