from Piece import *
from Bishop import *
from Rook import *


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♕" if color == "white" else "♛"

    def __str__(self):
        return f"{self.symbol} "

    def can_move(self, board, start_pos, end_pos):
        row_start, col_start = start_pos
        row_end, col_end = end_pos

        # Queen puede mover como Rook o como Bishop
        if not (Rook.can_move(self, board, start_pos, end_pos) or 
                Bishop.can_move(self, board, start_pos, end_pos)):
            return False

        return True