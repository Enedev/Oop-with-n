import random
class A:
  def f(self): #función print de A
    print("Soy A!")
class B:
  def f(self): #función print de B
    print("Soy B!")

a1 = A()
a2 = A()
b2 = B()
objects = [a1,a2,b2]
for i in objects:
  i.f() #se llamara a la función de cada clase -- tienen el mismo nombre pero se comprtan diferente