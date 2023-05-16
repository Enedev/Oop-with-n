from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field

@dataclass
class Animal(ABC):
    legs:int

    @abstractmethod
    def walk():
        pass

    @abstractmethod
    def eat():
        pass

@dataclass
class Pet(ABC):
    name: str

    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def setName():
        pass

@dataclass
class Spider(Animal):
    legs: int = field(init=False, default=8)

    def walk(self):
        return "Walk like a demon"

    def eat(self):
        return "eat HUMANS, FUCKING SPIDERS"

@dataclass
class Cat(Pet,Animal):
    legs: int = field(init=False, default=4)

    def getName(self):
        return f"my name is {self.name}"

    def setName(self, name):
        self.name = name
        return f"my new name is{self.name}, and i'm a cat"

    def walk(self):
        return "walk like a stupid god cat"

    def eat(self):
        return "eat the world because is a fat cat"

@dataclass
class Fish(Pet,Animal):
    legs: int = field(init=False, default=0)

    def getName(self):
        return f"my name is {self.name}, and i'm a fish"

    def setName(self, name):
        self.name = name
        return f"my new name is{self.name}"

    def walk(self):
        return "swim like a beautiful fish"

    def eat(self):
        return "eat fish food"
    
animal1 = Cat("Luna")

print(animal1)
animal2 = Fish("Nemo")
print(animal2)
animal3 = Spider()
print(animal3)

print(animal1.getName())
print(animal2.getName())
print(animal1.walk())
print(animal1.eat())
print(animal2.walk())
print(animal2.eat())
print(animal3.walk())
print(animal3.eat())

animal1.setName("Cabezon")
print(animal1)

