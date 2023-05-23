import pytest
from hi import Greeting

class TestGreeting:
    def test_greet(self):
        name = "John"
        print("Testing greet...")
        person = Greeting(name)
        print(person.greet())  # Agregado: Imprimir el saludo

    def test_greet_with_numbers(self):
        number = 12345
        person = Greeting(number)
        print(person.greet())  # Agregado: Imprimir el mensaje de error

    def test_greet_with_alphanumeric(self):
        alphanumeric = "john123"
        person = Greeting(alphanumeric)
        print(person.greet())  # Agregado: Imprimir el mensaje de error

    def test_greet_with_boolean(self):
        boolean = True
        person = Greeting(boolean)
        print(person.greet())  # Agregado: Imprimir el mensaje de error

