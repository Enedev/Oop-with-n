from garden import *

def main():
    #Creando el jardin con su tamaño
    garden = Garden(3)
    #Creando las plantas del jardin
    plantar = "aveces"
    while plantar != "no":
        row = int(input("Ingrese la fila para sembrar la planta: "))
        col = int(input("Ingrese la columna para sembrar la planta: "))
        type = input("Ingrese el tipo de planta (A o B): ")
        garden.plant(row, col, type)
        garden.print_garden()
        plantar = str(input("Desea continuar?, escriba no para salirse"))

    #Puesto por fuera del manejo del usuario para comprobar
    garden.plant(0, 1, "A")

    #Jardin terminado

    print("-------Ultimo tablero----------")
    garden.print_garden()

    #Regando el jardin
    print("--------Jardin Regado---------")
    garden.water()
    garden.print_garden()

if __name__ == '__main__':
    main()