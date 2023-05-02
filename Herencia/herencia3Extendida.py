class Animal: #clase base
  def __init__(self):
    print("Animal created...")
  def move(self):
    print("Animal moving...")

class Dog(Animal): #clase derivada
  def __init__(self):
    print("Dog created...")
  def move(self):
    print("Dog moving...")
  def bark(self):
    print("Barking!")

class Cat(Animal): #clase derivada
  def __init__(self):
    print("Cat created...")
  def move(self):
    print("Cat moving...")
  def meow(self):
    print("Meowing!")

animal = Animal()
dog = Dog()
cat = Cat()
print("-"*10)
animal.move()
dog.move() #método heredado
dog.bark()
cat.move() #método heredado

#No puedo hacer esto ombe
#dog.meow()
#animal.meow()