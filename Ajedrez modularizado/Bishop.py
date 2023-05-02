from Piece import *

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♗" if color == "white" else "♝"

    def __str__(self):
        return f"{self.symbol} "

    def can_move(self, board, start_pos, end_pos):
        # Comprabacion inicio y fin en la misma diagonal
        row_diff = abs(end_pos[0] - start_pos[0])
        col_diff = abs(end_pos[1] - start_pos[1])
        if row_diff != col_diff:
            return False

        # Comprobacion de que no hay piezas en la diagonal
        row_dir = 1 if end_pos[0] > start_pos[0] else -1
        col_dir = 1 if end_pos[1] > start_pos[1] else -1
        for i in range(1, row_diff):
            row = start_pos[0] + i * row_dir
            col = start_pos[1] + i * col_dir
            if board.get_piece((row, col)) is not None:
                return False

        return True