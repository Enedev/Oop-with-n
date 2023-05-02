#Movimiento invalido
class InvalidMoveException(Exception):
    pass

#Mover una pieza a una casilla ya ocupada
class OccupiedSquareException(Exception):
    pass

#Mover una pieza que no existe en la posicion dada
class NoPieceException  (Exception):
    pass

#No utiles ya que no esta implementado
#Mover una pieza que pertenece al contrario
class WrongColorException(Exception):
    pass

#Intenta mover en jaque
class KingInCheckException(Exception):
    pass