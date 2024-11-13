from typing import List
from clases.InterfazIterador import InterfazIterador


class IteradorResena(InterfazIterador):
    def __init__(self, elementos: List[object], filtros: List[object]):
        self.posicionActual = None
        self.elementos = elementos
        self.filtros = filtros

    def primero(self):
        self.posicionActual = 0

    def haTerminado(self):
        return self.posicionActual == (len(self.elementos) - 1)

    def siguiente(self):
        self.posicionActual += 1

    def actual(self):
        print(self.posicionActual)
        return self.posicionActual


    def cumpleFiltros(self):
        if self.sosDePeriodo(self.filtros[0], self.filtros[1]) and self.sosResenaPremium():
           return True
        return False