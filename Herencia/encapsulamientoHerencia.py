#Compartiendo al máximo las clases base
class A:
  def __init__(self):
    print("Creating A")
    self.a = "a" #miembro público -- +
    self.__x = "x" #miembro privado -- -
    self._y = "y" #miembro protegido -- #
  def __print_a(self): #método privado
    print("A!")
  def public_print(self): #método público
    self.__print_a()
class B(A): #clase derivada de A
  def __init__(self):
    super().__init__()
    print("Creating B")
    self.b = "b"
  def print_b(self):
    print("B!")
  def print_inherited_data(self):
    print(self._y)

b = B()
print(b.b)
print(b.a)
#print(b.x) #qué pasa?
print("-"*10)
b.print_inherited_data() #qué pasa?
print("-"*10)
a = A()
#a.__print_a() #qué pasa?
a.public_print() #qué pasa?