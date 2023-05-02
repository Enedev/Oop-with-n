class ExcAPOO(Exception):
  def __init__(self, mensaje):
    self.mensaje = mensaje

try:
  raise ExcAPOO("Gravísimo")
except ExcAPOO as e:
  print("Error! -->", e.mensaje)
except:
  print("Error genérico...")