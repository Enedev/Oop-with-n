from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass 
import random

@dataclass

class Customer(ABC):
    @abstractmethod
    def order(self):
        pass

    def tip(self):
        return random.randint(1, 5)

@dataclass
class VeganCustomer(Customer):
    def order(self):
        return "I'm having the vegan menu, please"

@dataclass
class NonVeganCustomer(Customer):

    def order(self):
        return "I want some steak!"
