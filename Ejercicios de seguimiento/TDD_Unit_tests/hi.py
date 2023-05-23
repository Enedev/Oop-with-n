from dataclasses import dataclass

@dataclass
class Greeting:
    name: str

    def greet(self):
        if isinstance(self.name, str) and self.name.isalpha():
            return f"Hello! Your name is {self.name}"
        elif isinstance(self.name, str) and not self.name.isalpha():
            return "ERROR ALPHANUMERIC: THE STRING CONTAINS NON-ALPHABETIC CHARACTERS"
        elif isinstance(self.name, int) or isinstance(self.name, float):
            return "ERROR Number"
        elif isinstance(self.name, bool):
            return "ERROR: YOU ENTERED A BOOLEAN"

name = "John"
person = Greeting(name)
print(person.greet())  # Agregado: Imprimir el saludo

number = 12345
person = Greeting(number)
print(person.greet())  # Agregado: Imprimir el mensaje de error

alphanumeric = "john123"
person = Greeting(alphanumeric)
print(person.greet())  # Agregado: Imprimir el mensaje de error

boolean = True
person = Greeting(boolean)
print(person.greet())  # Agregado: Imprimir el mensaje de error
