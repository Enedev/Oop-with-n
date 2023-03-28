class String:
      
    # inicializador (dunder method)
    def __init__(self, string):
      self.string = string
          
    def __repr__(self):
      return self.string
    
    def __add__(self, other):
      self.string += str(other)
      return self.string

  
# Código controlador
if __name__ == '__main__':
      
    # creando un objeto de tipo String
    string1 = String('Hello')
  
    # Dirección de memoria de objeto string1
    print(string1 + 5) #Qué imprime?

#Eq igualdad de objetos

class A(object):
  def __init__(self,a):
    self.a = a
  def __eq__(self, other):
      return self.a==other.a
class B():
  pass 
a = A(5)
b = B()
c = A(5)
print(a == c)#Qué imprime?