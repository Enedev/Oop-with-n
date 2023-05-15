from dataclasses import dataclass

@dataclass
class Vehiculo:
    marca: str
    modelo: str
    production_year: int
    _max_speed: float
    velocidad_actual:float = 0.00

    def get_max_speed(self):
        return self._max_speed
    
    def set_max_speed(self, value_max_speed):
        if(type(value_max_speed)==float):
            self._max_speed = value_max_speed
        else:
            print("Tipo de dato incorrecto...")

    def acelerar(self, segundos: int|float) -> float|int:
        velocidad_constante = 9.8
        
        if self.velocidad_actual <= self._max_speed:
            self.velocidad_actual = self.velocidad_actual + segundos*velocidad_constante

        return self.velocidad_actual
    
    def frenar(self, segundos: int|float) -> float|int:
        velocidad_constante = 9.8
        
        if self.velocidad_actual <= self._max_speed and self.velocidad_actual > 0:
            self.velocidad_actual = self.velocidad_actual - (segundos*velocidad_constante)

        return self.velocidad_actual

    def mostrar_datos(self):
        return '{' + self.marca + ', ' + self.modelo + ', ' + str(self.production_year) + ', ' + str(self._max_speed) + ', ' + str(self.velocidad_actual) + '}'




