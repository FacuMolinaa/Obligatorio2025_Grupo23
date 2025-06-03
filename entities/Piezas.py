class Pieza:
    def __init__(self, descripcion, costo, cantidad_disponible, registrar_pieza=False, listar_piezas=None):
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad_disponible = cantidad_disponible
        self.registrar_pieza = registrar_pieza
        self.piezas = []
        self.nombre_pieza = ""
        if listar_piezas is None:
            listar_piezas = [] 
    
    def registrar_costo_pieza(self, nombre_pieza, costo):
        self.costo = costo
        self.nombre_pieza = nombre_pieza
   
    def cantidad_pieza(self, nombre_pieza, cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible
        self.nombre_pieza = nombre_pieza
    
    def registrar_pieza(self):
        self.piezas.append(self)
        print(f"Pieza '{self.nombre_pieza}' registrada exitosamente.")
    
    def listar_piezas(self):
        return self.piezas