class Maquina:
    def __init__(self, id_maquina, requerimiento, descripcion, estado, disponibilidad=True):
        self.id_maquina = id_maquina
        self.descripcion = descripcion
        self.requerimiento = requerimiento
        self.nombre = f"Maquina {id_maquina}"
        self.estado = estado
        self.disponibilidad = disponibilidad
    def __str__(self):
        return f"Maquina(id_maquina={self.id_maquina}, nombre={self.nombre}, descripcion={self.descripcion}, estado={self.estado}, disponibilidad={self.disponibilidad})"