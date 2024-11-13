from typing import List
from Interfaces.InterfazIterador import InterfazIterador


class IteradorVinos(InterfazIterador):
    def __init__(self, elementos: List[object], filtros: List[object]):
        self.posicion_actual = None
        self.elementos = elementos
        self.filtros = filtros

    def primero(self):
        self.posicion_actual = 0

    def ha_terminado(self):
        return self.posicion_actual == (len(self.elementos) - 1)

    def siguiente(self):
        self.posicion_actual += 1

    def actual(self):
        print(self.posicion_actual)
        if self.elementos[self.posicion_actual].tenes_resenia_de_tipo_en_periodo:
            return self.elementos[self.posicion_actual]
        return False

    def cumple_filtros(self, filtros):
        pass
