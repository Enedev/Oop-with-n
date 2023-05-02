from abc import ABC, abstractmethod, abstractproperty

class Vehicle(ABC):

  @abstractmethod
  def move(self):
    pass
  
  @abstractmethod
  def stop(self):
    pass

  @property
  @abstractmethod
  def speed(self):
    pass
 
  def open_doors(self):
    print("opening doors...")

class ElectricCar(Vehicle): #clase concreta de Vehicle
  def move(self):
    print("moving...")

  def stop(self):
    print("stopping...")

  def speed(self):
    return 10

class GasCar(Vehicle): #clase concreta de Vehicle
  def __init__(self):
    self.speed = 100
  def move(self):
    print("Gas... moving...")

  def stop(self):
    print("Gas... stopping...")

  @property
  def speed(self):
    return self._speed
  @speed.setter
  def speed(self, speed_value):
    self._speed = speed_value

car = ElectricCar()
car.open_doors()
car.move()
car.stop()
print(car.speed)
car.speed = 100
print(car.speed)

print("-----")

car2 = GasCar()
car2.open_doors()
car2.move()
car2.stop()
print(car2.speed)
car2.speed = 900
print(car2.speed)