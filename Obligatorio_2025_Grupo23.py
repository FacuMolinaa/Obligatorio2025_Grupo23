class Sistema:
    def __init__(self,clientes,piezas,maquinas):
        self.clientes = clientes
        self.piezas = piezas
        self.maquinas = maquinas
        self.ordenes = []

class Piezas:
    def __init__(self,piezas):
        self.piezas=piezas