from persona import *

def f1(lista):
  
  lista.sort(key=lambda x: x._distance_traveled)

  return lista

def f2(lista):
   
  lista.sort(key=lambda x: len(x._name))

  return lista

def f3(lista, p_aux):
  
  for i in range(len(lista)):
    if p_aux._name == lista[i]._name and p_aux._age == lista[i]._age:
      return True
  return False

#def f3(lista_personas, persona_aux):
  #for persona in lista_personas:
    #if(persona == persona_aux):
      #return True
  #return False

def f4(lista):
  print(lista)
  
def f5(lista, name, age):
  new_person = Person(name, 1,age, 8)
  for i in lista:
    if i == new_person:
      lista.remove(i)
      return lista
  return lista
