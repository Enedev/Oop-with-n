#Compartiendo al maximo las clases base
class A:
  def __init__(self):
    print("Creating A")
    self.a = "a"
  def print_a(self):
    print("A!")
class B(A): #clase derivada de A
  def __init__(self):
    print("Creating B")
    self.b = "b"
  def print_b(self):
    print("B!")
class C(B): #clase derivada de B
  def __init__(self):
    B.__init__(self) #invocando constructor de B
    A.__init__(self) #invocando constructor de A
    print("Creating C")
    self.c = "c"
  def print_c(self):
    print("C!")

c = C() #qué pasa?
c.print_c()
c.print_b()
c.print_a()
print("--"*10)
print(c.c) #qué imprime?
print(c.b) #qué imprime?
print(c.a) #qué imprime?