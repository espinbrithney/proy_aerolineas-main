class Pasajero:
    def __init__(self, nombre, documento, asiento="", prioridad="Normal", estado="Confirmado"):
        self.nombre = nombre
        self.documento = documento
        self.asiento = asiento
        self.prioridad = prioridad
        self.estado = estado
        self.siguiente = None

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "documento": self.documento,
            "asiento": self.asiento,
            "prioridad": self.prioridad,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data.get("nombre", ""),
            documento=data.get("documento", ""),
            asiento=data.get("asiento", ""),
            prioridad=data.get("prioridad", "Normal"),
            estado=data.get("estado", "Confirmado"),
        )

    def __str__(self):
        return f"{self.nombre} ({self.documento}) - Asiento: {self.asiento or 'Sin asignar'} [{self.prioridad} | {self.estado}]"