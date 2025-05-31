class Pieza:
    def __init__(self, descripcion, costo, nombre_pieza, cantidad_disponible, registrar_pieza, listar_piezas):
        self.descripcion = descripcion
        self.costo = costo
        self.nombre_pieza = nombre_pieza
        self.cantidad_disponible = cantidad_disponible
        self.registrar_pieza = registrar_pieza
        self.es_registrada = False
        self.listar_piezas = listar_piezas


    def registrar_costo_pieza(self,nombre_pieza, costo):
        self.costo = costo
        self.nombre_pieza = nombre_pieza

    def cantidad_pieza(self, nombre_pieza, cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible
        self.nombre_pieza = nombre_pieza
    
    def registrar_pieza(self):
        self.registrada = True
        print(f"Pieza '{self.nombre_pieza}' registrada exitosamente.")

    def listar_piezas(self):
        if self.registrada:
            return f"Pieza: {self.nombre_pieza}, Descripción: {self.descripcion}, Costo: {self.costo}, Cantidad Disponible: {self.cantidad_disponible}"
        else:
            return "Pieza no registrada."

    