from dataclasses import dataclass 

@dataclass 
class Person:
  id:int
  name:str
  address:str
  phone:int

p1 = Person(1,"Arnulfo", "Cra xx", 12345)
print(p1.name)

@dataclass
class Tiki:
  id:int = -1
  name:str = "NN"
  address:str = "No tiene"
  phone:int = -1

p2 = Tiki()
print(p2.name) 