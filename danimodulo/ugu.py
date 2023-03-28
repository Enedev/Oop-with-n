from dataclasses import dataclass

@dataclass
class Vehiculo:
    name : str
    llantas: int

    def motocarro(self):
        if self.llantas == 3:
            return "es moto"
        elif self.llantas == 4:
            return "es carro"
        else:
            return "bobo pendejo"
        

    

