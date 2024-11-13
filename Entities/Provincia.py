from Entities.Pais import Pais


class Provincia:
    _provincias_instance = {}

    @classmethod
    def limpiar_instancias(cls):
        cls._provincias_instance.clear()

    def __new__(cls, id: int, nombre: str, pais: Pais):
        # Si la provincia ya existe por ID, devolver la instancia existente
        if id in cls._provincias_instance:
            return cls._provincias_instance[id]

        # Si no existe, crear una nueva instancia y guardarla en el diccionario
        instance = super().__new__(cls)
        cls._provincias_instance[id] = instance
        return instance

    def __init__(self, id: int, nombre: str, pais: Pais):
        # Asignar atributos solo la primera vez
        if not hasattr(self, 'id'):
            self.id = id
            self.nombre = nombre
            self.pais = pais

    # G/S for id
    def get_id(self):
        return self.id

    def set_id(self, id: int):
        self.id = id

    # G/S for nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    # G/S for pais
    def get_pais(self):
        return self.pais.get_nombre()

    def set_pais(self, pais: Pais):
        self.pais = pais
