class Error(Exception):
  def __init__(self):
    self.msg = "Mensaje base..."

class ExcAPOO(Error):
  def __init__(self, mensaje):
    Error.__init__(self)
    self.mensaje = mensaje

try:
  raise ExcAPOO("Error APOO")

except Error as e:
  print("1")
  print(e.mensaje)
  print(e.msg)
except ExcAPOO as e:
  print("2")
  print(e.msg)
  print(e.mensaje)