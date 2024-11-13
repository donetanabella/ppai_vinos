from abc import ABC, abstractmethod
from typing import List

class InterfazAgregado(ABC):
    @abstractmethod
    def crearIterador(self, elementos: List[object], Filtro: List[object]):
        pass
