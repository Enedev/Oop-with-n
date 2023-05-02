from Bishop import *
from King import *
from Knight import *
from Pawn import *
from Piece import *
from Queen import *
from Rook import *
from exceptions import *

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

        # Creamos las piezas blancas
        self.board[1] = [Pawn("white") for _ in range(8)]
        self.board[0][0] = Rook("white")
        self.board[0][1] = Bishop("white")
        self.board[0][2] = Knight("white")
        self.board[0][3] = Queen("white")
        self.board[0][4] = King("white")
        self.board[0][5] = Knight("white")
        self.board[0][6] = Bishop("white")
        self.board[0][7] = Rook("white")

        # Creamos las piezas negras
        self.board[6] = [Pawn("black") for _ in range(8)]
        self.board[7][0] = Rook("black")
        self.board[7][1] = Bishop("black")
        self.board[7][2] = Knight("black")
        self.board[7][3] = Queen("black")
        self.board[7][4] = King("black")
        self.board[7][5] = Knight("black")
        self.board[7][6] = Bishop("black")
        self.board[7][7] = Rook("black")

    def print_board(self):
        for row in self.board:
            row_str = "|"
            for piece in row:
                if piece is None:
                    row_str += "  |"
                else:
                    row_str += str(piece) + "|"
            print(row_str)

    def get_piece(self, pos):
        return self.board[pos[0]][pos[1]]

    def set_piece(self, pos, piece):
        self.board[pos[0]][pos[1]] = piece

    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece(start_pos)
        if piece is None:
            print("No hay pieza en la posición de inicio")
            #raise InvalidMoveException("No se puede mover ahi.")

            return False

        if not piece.can_move(self, start_pos, end_pos):
            print("La pieza no puede moverse a la posición de fin")
            #raise InvalidMoveException("No se puede mover ahi.")

            return False

        self.set_piece(start_pos, None)
        self.set_piece(end_pos, piece)
        return True