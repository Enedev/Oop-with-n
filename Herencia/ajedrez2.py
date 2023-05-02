class Piece:
    def __init__(self, color):
        self.color = color

    def can_move(self, board, start_pos, end_pos):
        # Método para comprobar si una pieza puede moverse a una determinada posición
        pass


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
            return False

        if not piece.can_move(self, start_pos, end_pos):
            print("La pieza no puede moverse a la posición de fin")
            return False

        self.set_piece(start_pos, None)
        self.set_piece(end_pos, piece)
        return True


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

#Cuadro de pruebas actualizado
print("--------------------------")
board.print_board()



