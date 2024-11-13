from Entities.Provincia import Provincia


class RegionVitivinicola:
    _regiones_instance = {}  # Diccionario para almacenar instancias únicas de RegionVitivinicola

    @classmethod
    def limpiar_instancias(cls):
        cls._regiones_instance.clear()

    def __new__(cls, id: int, nombre: str, provincia: Provincia):
        # Si la región ya existe por ID, devolver la instancia existente
        if id in cls._regiones_instance:
            return cls._regiones_instance[id]

        # Si no existe, crear una nueva instancia y guardarla en el diccionario
        instance = super().__new__(cls)
        cls._regiones_instance[id] = instance
        return instance

    def __init__(self, id: int, nombre: str, provincia: Provincia):
        # Asignar los atributos solo si la instancia no ha sido inicializada antes
        if not hasattr(self, 'id'):
            self.id = id
            self.nombre = nombre
            self.provincia = provincia
        
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

    # Get país
    def get_pais(self):
        return self.provincia.get_pais()
