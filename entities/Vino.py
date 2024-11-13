from datetime import datetime
from Entities.Bodega import Bodega
from Entities.Varietal import Varietal


class Vino:
    # Diccionario para almacenar instancias únicas
    _vinos_instance = {}

    @classmethod
    def limpiar_instancias(cls):
        cls._vinos_instance.clear()

    def __new__(cls, id: int, aniada: int, nombre: str, nota_de_cata_bodega: str, precio: int, bodega: Bodega):
        # Si el vino ya existe por ID, devolver la instancia existente
        if id in cls._vinos_instance:
            return cls._vinos_instance[id]

        # Si no existe, crear una nueva instancia y guardarla en el diccionario
        instance = super().__new__(cls)
        cls._vinos_instance[id] = instance
        return instance

    def __init__(self, id: int, aniada: int, nombre: str, nota_de_cata_bodega: str, precio: int, bodega: Bodega):
        self.id = id
        self.aniada = aniada
        self.nombre = nombre
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.precio = precio
        self.bodega = bodega
        self.varietales = set()
        self.resenias = set()

    # G/S for añada
    def get_aniada(self):
        return self.aniada

    def set_aniada(self, aniada: int):
        self.aniada = aniada

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

    # G/S for notaDeCataBodega
    def get_nota_de_cata_bodega(self):
        return self.nota_de_cata_bodega

    def set_nota_de_cata_bodega(self, nota_de_cata_bodega: str):
        self.nota_de_cata_bodega = nota_de_cata_bodega

    # G/S for precio
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    # G/S for bodega
    def get_bodega(self):
        return self.bodega

    def set_bodega(self, bodega: Bodega):
        self.bodega = bodega

    # G/S for varietal
    def get_varietal(self):
        return self.varietales

    def agregar_varietal(self, varietal: Varietal):
        self.varietales.add(varietal)

    # G/S for reseñas
    def get_resenias(self):
        return self.resenias

    def agregar_resenia(self, resenia):
        self.resenias.add(resenia)

    def tenes_resenia_de_tipo_en_periodo(self, fecha_desde: datetime, fecha_hasta: datetime):
        for resenia in self.resenias:
            if resenia.sos_de_periodo(fecha_desde, fecha_hasta) and resenia.sos_resenia_premium():
                return True
        return False

    def buscar_info_bodega(self):
        nombre_bodega = self.bodega.get_nombre()
        nombre_pais = self.bodega.obtener_region_y_pais()
        descripcion_varietal = []
        for varietal in self.varietales:
            descripcion_varietal.append(varietal.get_descripcion())
        return [nombre_bodega, nombre_pais, descripcion_varietal]

    def calcular_puntaje_resenia_en_periodo(self, fecha_desde: datetime, fecha_hasta: datetime):
        puntaje_acumulado = 0
        contador_resenias = 0
        promedio = 0
        for resenia in self.resenias:
            print(fecha_desde, fecha_hasta)
            print(resenia.sos_resenia_premium())
            if resenia.sos_resenia_premium() and resenia.sos_de_periodo(fecha_desde, fecha_hasta):
                print("entro")
                puntaje_acumulado += resenia.get_puntaje()
                contador_resenias += 1
                print(puntaje_acumulado)
                print(contador_resenias)
        if contador_resenias > 0:
            promedio = self.calcular_promedio(contador_resenias, puntaje_acumulado)
        return promedio

    def calcular_promedio(self, contador: int, puntaje_acumulado: int):
        promedio = puntaje_acumulado / contador
        print(promedio)
        return promedio
