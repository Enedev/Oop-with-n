from abc import ABC, abstractmethod, abstractproperty

from plant import *
from plantA import *
from plantB import *
from exceptions import *

class Garden:
    #Creacion del tablero
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.plants = []
    
    #Print al tablero
    def print_garden(self):
        for row in self.grid:
            print('|' + '|'.join(row) + '|')
    
    #Sembrar la planta
    def plant(self, row, col, plant_type):
        if not self._is_valid_position(row, col):
            raise ValueError('Posición inválida')

        if self.grid[row][col] != ' ':
            print('ya hay una planta')
            return
        
        if plant_type.lower() == 'a':
            new_plant = PlantA(row, col)
        elif plant_type.lower() == 'b':
            new_plant = PlantB(row, col)
        else:
            raise ValueError('Ya hay una planta')
        
        self.grid[row][col] = new_plant.seed
        self.plants.append(new_plant)
    
    #Regar el jardin
    def water(self):
        if not self.plants:
            raise ValueError('No hay plantas en el jardín')
        for plant in self.plants:
            plant.water()
            self.grid[plant.row][plant.col] = plant.seed
    
    #Posicion invalida
    def _is_valid_position(self, row, col):
        return row >= 0 and row < self.size and col >= 0 and col < self.size