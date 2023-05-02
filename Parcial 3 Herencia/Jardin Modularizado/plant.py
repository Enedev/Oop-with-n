from abc import ABC, abstractmethod
from dataclasses import dataclass 

#Clase abstracta de las plantas
@dataclass
class Plant(ABC):
    row: int
    col: int
    seed = ' '
    
    #Sembrar
    @abstractmethod
    def grow(self):
        pass
    
    #Regar
    @abstractmethod
    def water(self):
        pass