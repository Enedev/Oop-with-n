from Board import *

def main():
    # Creamos un tablero y lo imprimimos
    board = Board()
    board.print_board()

    #Moviendo Peones
    #Blancos:
    board.move_piece((6,1),(5,2))
    board.move_piece((6,5),(5,5))
    board.move_piece((6,7),(5,7))

    #Negros:
    board.move_piece((1,0),(2,0))
    board.move_piece((1,5),(2,5))
    board.move_piece((1,7),(2,7))

    #Moviendo a los caballos blancos
    board.move_piece((7,2),(5,1))
    board.move_piece((7,5),(5,6))

    #Moviendo a los caballos negros
    board.move_piece((0,2),(2,1))
    board.move_piece((0,5),(2,4))

    # Tablero Actualizado
    print("--------------------------")
    board.print_board()

    #Moviendo peones para poder mover otras fichas
    board.move_piece((6,2),(5,2))

    #Moviendo Alfiles Blancos
    board.move_piece((7,1),(4,4))
    board.move_piece((7,6),(6,5))

    #Moviendo ALfiles Negros
    board.move_piece((0,1),(1,0))
    board.move_piece((0,6),(1,7))

    #Moviento torres blancas
    board.move_piece((7,7),(6,7))

    #Moviendo torres negras
    board.move_piece((0,0),(0,2))

    #Moviendo a la reina blanca
    board.move_piece((7,3),(6,2))

    #Segundo tablero actualizado
    print("--------------------------")
    board.print_board()

    #Devolviendo a la torre para poder mover la reina negra 
    board.move_piece((0,2),(0,0))

    #Moviendo a la reina negra
    board.move_piece((0,3),(0,1))

    #Moviendo a los reyes
    board.move_piece((7,4),(7,3))
    board.move_piece((0,4),(0,5))
    board.move_piece((0,5),(1,5))

    #Tercer tablero actualizado
    print("--------------------------")
    board.print_board()

    #Pruebas de choque
    #Elimina al otro alfin 
    board.move_piece((1,7),(4,4))
    #Y luego se devuelve borrando a la que estaba anterior
    board.move_piece((4,4),(3,5))

    #Prueba de peones, no deja comerse a ninguno
    board.move_piece((2,0),(3,0))
    board.move_piece((2,0),(3,0))
    board.move_piece((3,0),(4,0))
    board.move_piece((4,0),(5,0))
    board.move_piece((5,0),(6,0))

    board.move_piece((2,7),(3,7))

    #Comprobando torre
    board.move_piece((0,7),(2,7))
    board.move_piece((2,7),(2,6))
    # Se come la pieza
    board.move_piece((2,6),(5,6))
    #Se devuelve
    board.move_piece((5,6),(4,6))

    #Cuadro de pruebas actualizado
    print("--------------------------")
    board.print_board()

if __name__ == '__main__':
    main()