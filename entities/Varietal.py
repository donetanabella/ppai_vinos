class Varietal:
    # Diccionario para almacenar instancias únicas de uva
    _varietal_instances = {}

    def __new__(cls, id: int, descripcion: str):
        # chequea si se creó el varietal antes
        if id in cls._varietal_instances:
            return cls._varietal_instances[id]

        instance = super().__new__(cls)
        cls._varietal_instances[id] = instance
        return instance

    def __init__(self, id: int, descripcion: str):
        self.descripcion = descripcion
        if not hasattr(self, "id"):
            self.id = id
            self.descripcion = descripcion

    # G/S for descripcion
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion
