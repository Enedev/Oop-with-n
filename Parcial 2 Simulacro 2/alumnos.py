from dataclasses import dataclass
from typing import *

@dataclass
class Alumno:
    _name : str
    _age: int
    _notes: List[float]

    def promedio(self):
        aux = 0
        for i in range(len(self._notes)):
            aux += self._notes[i]
        return aux / len(self._notes)
    
    def nota_mayor(self):
        sorted_notes = sorted(self._notes)
        return self._notes[0]
    
    def nota_menor(self):
        sorted_notes = sorted(self._notes)
        return self._notes[-1]
            

