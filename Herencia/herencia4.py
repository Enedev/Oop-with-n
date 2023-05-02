class Animal: #clase base
  def __init__(self):
    print("Animal created...")
    self.legs = None

  def move(self):
    print("Animal moving...")

class Dog(Animal): #clase derivada
  def __init__(self, age):
    Animal.__init__(self) #invocando al constructor de la clase base - modo 1
    print("Dog created...")
    self.age = age
  def move(self):
    print("Dog moving...")
  def bark(self):
    print("Barking!")

class Cat(Animal): #clase derivada
  def __init__(self, color):
    super().__init__() #invocando al constructor de la clase base - modo 2
    print("Cat created...")
    self.color = color
  def move(self):
    print("Cat moving...")
  def meow(self):
    print("Meowing!")


dog = Dog(5)
cat = Cat("black")
print("-"*10)

print(dog.legs)

dog.legs = 50 #cambiando valor de un atributo heredado
cat.legs = 4 #cambiando valor de un atributo heredado


print(cat.legs)
print(dog.legs)