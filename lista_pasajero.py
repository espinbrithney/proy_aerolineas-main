from pasajero import Pasajero


class ListaPasajeros:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    # 1. Insertar al final
    def agregar_al_final(self, pasajero):
        if not isinstance(pasajero, Pasajero):
            pasajero = Pasajero(**pasajero)
        pasajero.siguiente = None
        if self.cabeza is None:
            self.cabeza = pasajero
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = pasajero
        self.tamano += 1
        return pasajero

    # 2. Insertar al inicio
    def agregar_al_inicio(self, pasajero):
        if not isinstance(pasajero, Pasajero):
            pasajero = Pasajero(**pasajero)
        pasajero.siguiente = self.cabeza
        self.cabeza = pasajero
        self.tamano += 1
        return pasajero

    # 3. Insertar en una posición (índice 0-based)
    def insertar_en_posicion(self, indice, pasajero):
        if not isinstance(pasajero, Pasajero):
            pasajero = Pasajero(**pasajero)
        if indice <= 0 or self.cabeza is None:
            return self.agregar_al_inicio(pasajero)
        actual = self.cabeza
        pos = 0
        while actual.siguiente is not None and pos < indice - 1:
            actual = actual.siguiente
            pos += 1
        pasajero.siguiente = actual.siguiente
        actual.siguiente = pasajero
        self.tamano += 1
        return pasajero

    # 4. Eliminar por documento
    def eliminar_por_documento(self, documento):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.documento == documento:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamano -= 1
                return actual
            anterior = actual
            actual = actual.siguiente
        return None

    # 5. Buscar por documento
    def buscar_por_documento(self, documento):
        actual = self.cabeza
        while actual is not None:
            if actual.documento == documento:
                return actual
            actual = actual.siguiente
        return None

    # 6. Actualizar datos por documento
    def actualizar_pasajero(self, documento, nombre=None, asiento=None, prioridad=None, estado=None):
        pasajero = self.buscar_por_documento(documento)
        if pasajero is None:
            return None
        if nombre is not None:
            pasajero.nombre = nombre
        if asiento is not None:
            pasajero.asiento = asiento
        if prioridad is not None:
            pasajero.prioridad = prioridad
        if estado is not None:
            pasajero.estado = estado
        return pasajero

    # 7. Listar todos los pasajeros como lista de objetos
    def listar_pasajeros(self):
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(actual)
            actual = actual.siguiente
        return elementos

    # 8. Contar total de pasajeros
    def contar_pasajeros(self):
        return self.tamano

    # 9. Convertir toda la lista a lista de diccionarios (para JSON)
    def to_list(self):
        return [p.to_dict() for p in self.listar_pasajeros()]

    def cargar_desde_lista(self, lista_dicts):
        self.cabeza = None
        self.tamano = 0
        for item in lista_dicts or []:
            self.agregar_al_final(Pasajero.from_dict(item))