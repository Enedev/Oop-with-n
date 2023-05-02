from plant import *

#Planta A
class PlantA(Plant):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.seed = 'a'
    
    #Cuando esta regada

    def grow(self):
        self.seed = '*'
    
    #Regar
    def water(self):
        self.grow()