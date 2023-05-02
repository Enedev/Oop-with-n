from Piece import *
    
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♖" if color == "white" else "♜"

    def __str__(self):
        return f"{self.symbol} "
    
    def can_move(self, board, start_pos, end_pos):
        # Comprobamos si la posición de fin está ocupada por una pieza del mismo color
        if board.get_piece(end_pos) is not None and board.get_piece(end_pos).color == self.color:
            return False

        # Comprobamos si el movimiento es horizontal o vertical
        if start_pos[0] != end_pos[0] and start_pos[1] != end_pos[1]:
            return False

        # Comprobamos que no haya ninguna pieza en el camino
        if start_pos[0] == end_pos[0]:
            for col in range(min(start_pos[1], end_pos[1])+1, max(start_pos[1], end_pos[1])):
                if board.get_piece((start_pos[0], col)) is not None:
                    return False
        else:
            for row in range(min(start_pos[0], end_pos[0])+1, max(start_pos[0], end_pos[0])):
                if board.get_piece((row, start_pos[1])) is not None:
                    return False

        return True
