class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, x, y):
        if self.can_move(x, y):
            self.x = x
            self.y = y
            return True
        return False
    
    def can_move(self, x, y):
        return True
        
class Pawn(Piece):
    def can_move(self, x, y):
        if x == self.x and y == self.y + 1:
            return True
        return False
        
class Bishop(Piece):
    def can_move(self, x, y):
        if abs(x - self.x) == abs(y - self.y):
            return True
        return False
        
class Rook(Piece):
    def can_move(self, x, y):
        if x == self.x or y == self.y:
            return True
        return False
        
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        
    def add_piece(self, piece):
        self.board[piece.y][piece.x] = piece
        
    def display(self):
        for row in self.board:
            for piece in row:
                if piece is None:
                    print("-", end=" ")
                else:
                    print(piece.__class__.__name__[0], end=" ")
            print()
        print()
        
board = Board()
board.add_piece(Pawn(1, 1))
board.add_piece(Bishop(2, 2))
board.add_piece(Rook(0, 0))
board.display()

board.board[1][1].move(1, 2)
board.board[2][2].move(4, 4)
board.board[0][0].move(5, 0)

board.display()
