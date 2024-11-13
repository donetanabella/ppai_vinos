from RegionVitivinicola import RegionVitivinicola


class Bodega:
    _bodegas_instance = {}

    def __new__(cls, id: int, nombre: str, descripcion: str, region: RegionVitivinicola):
        # Si la bodega ya existe por ID, devolver la instancia existente
        if id in cls._bodegas_instance:
            return cls._bodegas_instance[id]

        # Si no existe, crear una nueva instancia y guardarla en el diccionario
        instance = super().__new__(cls)
        cls._bodegas_instance[id] = instance
        return instance

    def __init__(self, id: int, descripcion: str, nombre: str, region: RegionVitivinicola):
        # Asignar id, descripcion, nombre y region solo la primera vez
        if not hasattr(self, 'id'):
            self.id = id
            self.descripcion = descripcion
            self.nombre = nombre
            self.region = region

    # G/S for nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    # G/S for descripcion
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion

    # G/S for region
    def get_region(self):
        return self.region

    def set_region(self, region: RegionVitivinicola):
        self.region = region

    def obtener_region_y_pais(self):
        return [self.get_region().get_nombre(), self.get_region().get_pais()]
