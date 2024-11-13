class Pais:
    _paises_instance = {}  # Diccionario para almacenar instancias únicas de Pais

    @classmethod
    def limpiar_instancias(cls):
        cls._paises_instance.clear()

    def __new__(cls, id: int, nombre: str):
        # Si el país ya existe por ID, devolver la instancia existente
        if id in cls._paises_instance:
            return cls._paises_instance[id]

        # Si no existe, crear una nueva instancia y guardarla en el diccionario
        instance = super().__new__(cls)
        cls._paises_instance[id] = instance
        return instance

    def __init__(self, id: int, nombre: str):
        # Asignar atributos solo la primera vez
        if not hasattr(self, 'id'):
            self.id = id
            self.nombre = nombre

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
