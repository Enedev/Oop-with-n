#creacion
class Students(object):
  def __init__(self, id, grade):
    self.id = id
    self.grade = grade
  def __new__(cls, id, grade):
    print("Creando instancia")
    instance = super(Students, cls).__new__(cls)
    if 5 <= grade <= 10:
        return instance
    else:
        return None
  def __repr__(self): #método especial para conversión de tipo
    return f"{self.__class__.__name__}  {self.__dict__}"

stud1 = Students(1, 7)
print(stud1) #Qué imprime?
 
stud2 = Students(2, 12)
print(stud2)#Qué imprime?

#destruccion
class A(object):
    def __del__(self):
        print('Destroyed')
 
A() #Qué imprime? #ob1
x=A() #Qué imprime? #obj2