from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    quantity: int

@dataclass
class Dish:
    name: str
    ingredients: dict

class Chef:
    def __init__(self, name):
        self.name = name

    def verify_dish(self, dish):
        print(f"El chef {self.name} está verificando el plato: {dish.name}")

class SubChef(Chef):
    def __init__(self, name, chef):
        super().__init__(name)
        self.chef = chef
        self.occupied = False

    def deliver_dish(self, dish):
        print(f"El subchef {self.name} entrega el plato: {dish.name} al cliente")
        self.occupied = False

class Restaurant:
    def __init__(self):
        self.ingredients = {}
        self.menu = []
        self.chef = Chef("Chef Principal")
        self.subchefs = [SubChef("Subchef 1", self.chef), SubChef("Subchef 2", self.chef)]

    def add_ingredient(self, name, quantity):
        ingredient = Ingredient(name, quantity)
        self.ingredients[name] = ingredient

    def add_dish(self, name, ingredients):
        dish = Dish(name, ingredients)
        self.menu.append(dish)

    def make_order(self, dish_name):
        dish = next((dish for dish in self.menu if dish.name == dish_name), None)
        if dish is None:
            print("El plato solicitado no está en el menú.")
            return

        for ingredient, quantity in dish.ingredients.items():
            if ingredient not in self.ingredients or self.ingredients[ingredient].quantity < quantity:
                print(f"No hay suficiente {ingredient} para preparar el plato.")
                return

        for ingredient, quantity in dish.ingredients.items():
            self.ingredients[ingredient].quantity -= quantity

        self.chef.verify_dish(dish)

        # Obtener el subchef disponible 1
        subchef1 = self.get_available_subchef()
        if subchef1 is None:
            print("No hay subchefs disponibles en este momento.")
            return

        subchef1.deliver_dish(dish)

        # Obtener el subchef disponible 2
        subchef2 = self.get_available_subchef()
        if subchef2 is None:
            print("No hay subchefs disponibles en este momento.")
            return

        subchef2.deliver_dish(dish)

        self.customer_eat(dish)
        self.customer_pay(dish)

    def get_available_subchef(self):
        for subchef in self.subchefs:
            if not subchef.occupied:
                subchef.occupied = True
                return subchef
        return None

    def customer_eat(self, dish):
        print(f"El cliente está comiendo el plato: {dish.name}")

    def customer_pay(self, dish):
        print(f"El cliente paga el plato: {dish.name}")

    def display_menu(self):
        print("Menú del restaurante:")
        for dish in self.menu:
            print(f"- {dish.name}")

    def display_inventory(self):
        print("Inventario del restaurante:")
        for ingredient, data in self.ingredients.items():
            print(f"- {ingredient}: {data.quantity}")
                                 
# Crear una instancia del restaurante
restaurant = Restaurant()

# Agregar ingredientes al inventario
restaurant.add_ingredient("Tomate", 10)
restaurant.add_ingredient("Cebolla", 5)
restaurant.add_ingredient("Pimiento", 7)

# Agregar platos al menú
restaurant.add_dish("Ensalada", {"Tomate": 2, "Cebolla": 1})
restaurant.add_dish("Pimientos rellenos", {"Pimiento": 3, "Cebolla": 2})

# Mostrar el menú y el inventario
restaurant.display_menu()
restaurant.display_inventory()

# Realizar un pedido
restaurant.make_order("Ensalada")
restaurant.subchefs[0].occupied = True
print("----------------------------------------------------------------------")
restaurant.make_order("Pimientos rellenos")


# Mostrar el inventario actualizado
restaurant.display_inventory()