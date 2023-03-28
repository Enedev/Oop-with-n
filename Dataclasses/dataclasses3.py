from dataclasses import dataclass
from dataclasses import astuple, asdict

@dataclass
class C:
  a: int = 88
  b: int = 99

c = C()
print(astuple(c)) #representación en tupla
print(asdict(c)) #representación en diccionario


from dataclasses import astuple, asdict

@dataclass(frozen = True)
class C:
  a: int = 88
  b: int = 99

c = C()
c.a = 100 #--> error de tipo frozen instance