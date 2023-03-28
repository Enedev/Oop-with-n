from vehiculo import *

def main():
  vehiculo1 = Vehiculo("Ford", "Mustang", 2022, 250.0)
  vehiculo1.acelerar(10)
  print(vehiculo1.mostrar_datos())
  vehiculo1.frenar(5)
  print(vehiculo1.mostrar_datos())
  
if __name__ == "__main__":
  main()