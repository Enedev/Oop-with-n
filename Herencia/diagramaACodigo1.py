from dataclasses import dataclass

@dataclass
class Person:
  name: str 
  age: int 
  size: float 
  hair_color: str  
  
  def walk(self, distance: int):
    print(f"{self.name} está caminando {distance} kms...")

  def eat(self, food: str):
    print(f"{self.name} está comiendo {food}")
  
  def speak(self, language: str):
    print(f"{self.name} está hablando {language}")

@dataclass
class Student(Person):
  subject: str

  def study(self, subject: str):
    print(f"{self.name} está estudiando")

class Teacher(Person):
  def teach(self, subject: str):
    print(f"{self.name} está enseñando")

p1 = Person("p1", 5, 1.8, "c1")
p2 = Person("p2", 6, 1.9, "c2")
s1 = Student("s1", 6, 1.9, "c2", "math")
t1 = Teacher("t1", 8, 1.6, "c4")

s1.walk(50)
s1.name
s1.subject