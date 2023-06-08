from dataclasses import dataclass
from customer import *
import pickle
from creator import *
from typing import List


@dataclass
class RestaurantCoordinator:
    customers: List[Customer]
    tables: List[Table]


    def create_customers(self):
        customers = []
        with open("customer_reservations.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("Customer"):
                    parts = line.split(", ")
                    customer_type = parts[1]
                    if customer_type == "vegan":
                        customer = VeganCustomer()
                    elif customer_type == "non-vegan":
                        customer = NonVeganCustomer()
                    else:
                        raise ValueError(f"Invalid customer type: {customer_type}")
                    customers.append(customer)
        return customers
    
    

    def deserializacion(self):
        with open("table_data.pickle", "rb") as file:
            table_contents = pickle.load(file)
        return table_contents
    
    def create_tables(self):
        for i in range(1, 26):
            capacity = random.randint(1, 4)
            table = Table(i, capacity, [])  
            self.tables.append(table)

    def assign_tables(self):
        for customer in self.customers:
            assigned = False
            for table in self.tables:
                if len(table.customer_list) + 1 <= table.capacity:
                    table.customer_list.append(customer)
                    assigned = True
                    break
            if not assigned:
                raise Exception("Your reservation is cancelled!")

    def print_table_report(self):
        for table in self.tables:
            tip_total = sum(customer.tip() for customer in table.customer_list)
            print(f"Table {table.id} --> tip: ${tip_total}")
        
    

@dataclass
class Waiter:
    def __init__(self, tables: List[Table]):
        self.tables = tables

    def take_orders(self):
        for table in self.tables:
            print(f"Table {table.id}:")
            for customer in table.customer_list:
                print(customer.order())
                print(customer.tip())

    def generate_tip_report(self):
        for table in self.tables:
            if table.customer_list:
                tip_total = sum(customer.tip() for customer in table.customer_list)
                print(f"Table {table.id} --> tip: ${tip_total}")
            else:
                print(f"Table {table.id} --> tip: $0")

coordinator = RestaurantCoordinator(customers=[], tables=[])
customers = coordinator.create_customers()
coordinator.create_tables()
coordinator.assign_tables()

for customer in customers:
    print(customer.order())
    print(customer.tip())

print(coordinator.deserializacion())

waiter = Waiter(coordinator.tables)
waiter.take_orders()
waiter.generate_tip_report()