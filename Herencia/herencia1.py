class Animal: #clase padre, clase madre, clase base
  def __init__(self):
    print("Animal created...")
  def move(self):
    print("Animal moving...")

class Dog(Animal): #clases hijas, clases derivadas
  pass

class Cat(Animal):
  pass

animal = Animal()
dog = Dog()
cat = Cat()
print("-"*10)
animal.move()
dog.move() #método heredado
cat.move() #método heredado