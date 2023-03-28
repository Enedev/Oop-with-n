from dataclasses import dataclass 

class A:
  pass

@dataclass
class B:
  pass

a = A()
b = B()
print(a)
print(b)


@dataclass
class C:
  a: int = 88
  b: int = 99

  def __repr__(self): #la dataclass sigue siendo una clase, así que todos sus métodos de instancia llevan "self"
    return f"en a -> {self.a} y en b->{self.b}" #acceso mediante self porque SON atributos de la clase

c = C()
print(c)