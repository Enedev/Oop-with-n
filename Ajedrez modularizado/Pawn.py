from Piece import *

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♙" if color == "white" else "♟"

    def __str__(self):
        return f"{self.symbol} "
    

    def can_move(self, board, start_pos, end_pos):
    # Comprobamos si la posición de fin está ocupada
        if board.get_piece(end_pos) is not None:
            return False

        # Comprobamos si el movimiento es hacia adelante
        if self.color == "white":
            if start_pos[0] == 1 and end_pos[0] == 3 and start_pos[1] == end_pos[1] and board.get_piece((2, start_pos[1])) is None:
                # Si el peón blanco está en la segunda fila y se mueve dos casillas hacia adelante,
                # comprobamos que la casilla intermedia esté vacía
                return True
            elif start_pos[0] + 1 != end_pos[0] or start_pos[1] != end_pos[1]:
                # Si el peón blanco no se mueve hacia adelante una casilla, o se mueve hacia los lados,
                # el movimiento no es válido
                return False
        else:
            if start_pos[0] == 6 and end_pos[0] == 4 and start_pos[1] == end_pos[1] and board.get_piece((5, start_pos[1])) is None:
                # Si el peón negro está en la séptima fila y se mueve dos casillas hacia adelante,
                # comprobamos que la casilla intermedia esté vacía
                return True
            elif start_pos[0] - 1 != end_pos[0] or start_pos[1] != end_pos[1]:
                # Si el peón negro no se mueve hacia adelante una casilla, o se mueve hacia los lados,
                # el movimiento no es válido
                return False

        return True