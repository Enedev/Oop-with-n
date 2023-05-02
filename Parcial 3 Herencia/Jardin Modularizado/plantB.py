from plant import *

#Planta B
class PlantB(Plant):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.seed = 'b'
    
    #Cuando esta regada
    def grow(self):
        self.seed = '#'
    
    #Regar
    def water(self):
        self.grow()
