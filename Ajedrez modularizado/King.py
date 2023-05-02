from Piece import *

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♔" if color == "white" else "♚"

    def __str__(self):
        return f"{self.symbol} "

    def can_move(self, board, start_pos, end_pos):
        # Comprobamos si la posición de fin está ocupada por una pieza del mismo color
        if board.get_piece(end_pos) is not None and board.get_piece(end_pos).color == self.color:
            return False

        row_diff = abs(end_pos[0] - start_pos[0])
        col_diff = abs(end_pos[1] - start_pos[1])

        # Comprobamos si el movimiento es diagonal, horizontal o vertical
        if row_diff > 1 or col_diff > 1 or (row_diff == 0 and col_diff == 0):
            return False

        return True