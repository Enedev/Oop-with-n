#getters y setters para gestionar los miembros privados
class Person:
  def __init__(self, name, id):
    self.__name = name #atributo privado
    self.__id = id #atributo privado

  def set_name(self, name_value):
    if(type(name_value)==str):
      self.__name = name_value
    else:
      print("Grave...")
  def get_name(self):
    return self.__name
  def set_id(self, id_value):
    self.__id = id_value
  def get_id(self):
    return self.__id

p = Person("Magola", 123)
print(p.get_name()) #acceso a través de un método público
p.set_name(666) #acceso a través de un método público
print(p.get_name()) #acceso a través de un método público