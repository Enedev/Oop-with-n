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


class Cat(Animal): #clase derivada
  def __init__(self):
    print("Cat created...")
  def move(self):
    print("Cat moving...")

animal = Animal()
dog = Dog()
cat = Cat()
print("-"*10)
animal.move()
dog.move() #método heredado
cat.move() #método heredado

print(type(animal))
print(type(cat))
print(type(dog))

print(isinstance(animal, Animal))
print(isinstance(cat, Cat))
print(isinstance(dog, Dog))
print(isinstance(cat, Animal))  

print("-"*10)

print(issubclass(type(animal), Animal))
print(issubclass(type(cat), Dog))
print(issubclass(type(dog), Dog))
print(issubclass(type(cat), Animal))   