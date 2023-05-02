from dataclasses import dataclass
from typing import *

@dataclass
class Alumno:
    _name : str
    _age: int
    _notes: List[float]

    def __repr__(self) -> str:
        return '{' + self._name + ', ' + str(self._age) + '}'
    
    def get_notes(self):
        return self._notes
    
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
    
def mejores_alumnos(students_list):
    aux : List[object] = []
    aux1 : float = 0
    aux2 : List[float] = []

    for i in range(len(students_list)):
        aux.append(students_list[i].get_notes())

    for row in aux:
        for elem in row:
            aux1 += elem  
        aux2.append(aux1/len(aux[0]))
        aux1 : float = 0

    d = list(zip(students_list, aux2))

    sorted_d = sorted(d, key=lambda x: -x[1])
    return sorted_d[0], sorted_d[1], sorted_d[2]
            

