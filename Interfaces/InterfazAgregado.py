from abc import ABC, abstractmethod
from typing import List


class InterfazAgregado(ABC):
    @abstractmethod
    def crear_iterador(self, elementos: List[object], filtro: List[object]):
        pass
