from Piece import *

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♘" if color == "white" else "♞"

    def __str__(self):
        return f"{self.symbol} "
        
    def can_move(self, board, start_pos, end_pos):
        # Comprobamos si la posición de fin está ocupada por una pieza del mismo color
        if board.get_piece(end_pos) is not None and board.get_piece(end_pos).color == self.color:
            return False

        # Comprobamos si el movimiento es en L
        x_diff = abs(start_pos[0] - end_pos[0])
        y_diff = abs(start_pos[1] - end_pos[1])
        if not ((x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)):
            return False

        return True