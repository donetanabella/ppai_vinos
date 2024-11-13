from datetime import datetime

from clases.entities import Vino


class Resena:
    def __init__(self, id: int, comentario: str, es_premium: bool, fecha_resenia: datetime, puntaje: int, vino: Vino):
        self.id = id
        self.comentario = comentario
        self.es_premium = es_premium
        self.fecha_resenia = fecha_resenia
        self.puntaje = puntaje
        # hacer diccionario de Vinos
        self.vino = vino
        vino.agregar_resenia(self)

    # G/S for id
    def get_id(self):
        return self.id

    def set_id(self, id: int):
        self.id = id

    # G/S for comentario
    def get_comentario(self):
        return self.comentario

    def set_comentario(self, comentario: str):
        self.comentario = comentario

    # G/S for es_premium
    def get_es_premium(self):
        return self.es_premium

    def set_es_premium(self, premium: bool):
        self.es_premium = premium

    # G/S for fecha_resenia
    def get_fecha_resenia(self):
        return self.fecha_resenia

    def set_fecha_resenia(self, date: datetime):
        self.fecha_resenia = date

    # G/S for puntaje
    def get_puntaje(self):
        return self.puntaje

    def set_puntaje(self, puntaje: int):
        self.puntaje = puntaje

    def sos_de_periodo(self, fecha_desde: datetime, fecha_hasta: datetime):
        print(self.fecha_resenia)
        return fecha_desde <= self.fecha_resenia <= fecha_hasta

    def sos_resenia_premium(self):
        return self.es_premium
