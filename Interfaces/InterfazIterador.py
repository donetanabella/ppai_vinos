from abc import ABC, abstractmethod
from typing import List

class InterfazIterador(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def primero(self):
        pass
    
    @abstractmethod
    def siguiente(self):
        pass
    
    @abstractmethod
    def haTerminado(self):
        pass
    
    @abstractmethod
    def actual(self):
        pass
    
    @abstractmethod
    def cumpleFiltros(self, filtros: List[object]):
        pass
    
    