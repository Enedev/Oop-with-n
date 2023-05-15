from vehiculo import *
from conductor import *

def main():
  vehiculo1 = Vehiculo("Ford", "Mustang", 2022, 250.0)
  vehiculo1.acelerar(10)
  print(vehiculo1.mostrar_datos())
  vehiculo1.frenar(5)
  print(vehiculo1.mostrar_datos())

  conductor1 = Conductor("Arnulfo")
  print(conductor1.conducir_auto(vehiculo1))
  
if __name__ == "__main__":
  main()