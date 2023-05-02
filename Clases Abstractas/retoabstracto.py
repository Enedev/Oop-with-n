from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass 

@dataclass
class Employee(ABC):
    
    first_name:str
    last_name:str

    def full_name(self):
            print(full_name = self.first_name + " " + self.last_name)

    @abstractmethod
    def get_salary(self):
        pass


@dataclass
class hourlyEmployee(Employee):
    worked_hours: int
    rate: int

    def get_salary(self):
        return self.worked_hours * self.rate


@dataclass
class fullTimeEmployee(Employee):
    salary: float

    def get_salary(self):
        return self.salary
    
hourlyEmployee = hourlyEmployee("Neithan", "Gomez", 10, 2)
fullTimeEmployee = fullTimeEmployee("Neithan", "Gomez", 231)

print(hourlyEmployee.get_salary())
print(fullTimeEmployee.get_salary())