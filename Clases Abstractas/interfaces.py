from abc import ABC, abstractmethod, abstractproperty
class A:
  def a(self):
    print("a")
  def b(self):
    print("b")
class C(ABC): #interfaz
  @abstractmethod
  def c():
    pass
  @abstractmethod
  def d():
    pass
class B(A,C):
  #implementar los métodos abstractos heredados -->interfaz
  def c(self):
    print("c")
  def d(self):
    print("d")

b = B()
b.a()
b.b()
b.c()
b.d()