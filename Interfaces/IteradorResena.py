from typing import List
from Interfaces.InterfazIterador import InterfazIterador

from Entities.Resena import Resena


class IteradorResena(InterfazIterador):
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
        return self.posicion_actual


    def cumple_filtros(self):
        if self.sosDePeriodo(self.filtros[0], self.filtros[1]) and self.sosResenaPremium():
           return True
        return False
