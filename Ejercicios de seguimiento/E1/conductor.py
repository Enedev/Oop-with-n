from dataclasses import dataclass
from vehiculo import *

@dataclass
class Conductor:
    name: str

    def conducir_auto(self, auto):
        auto.acelerar(5)
        return auto.mostrar_datos()
        
        
    

