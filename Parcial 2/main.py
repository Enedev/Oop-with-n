from persona import *
from principal import *

def main():
  p1 = Person("Person 1", 1,10, 5)
  p2 = Person("per 2", 1,11, 10)
  p3 = Person("person 3", 1,5, 11)
  p4 = Person("persona 4", 1,10, 8)
  lista_personas = [p1,p2,p3,p4]

  print("antes de f1",lista_personas)
  print("después de f1",f1(lista_personas) )
  print("-"*10)

  #f2
  print("antes de f2",lista_personas)
  print("después de f2",f2(lista_personas))
  print("-"*10)

  #f3
  print("f3", f3(lista_personas, p4))
  print("-"*10)

  #f4
  print("f4", end =" ")
  f4(lista_personas)
  print("-"*10)

  #f5
  print("f5", f5(lista_personas, "persona 4", 10))
  print("-"*10)
  
if __name__ == "__main__":
  main()