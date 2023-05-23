import pickle
from dataclasses import dataclass

def process_data(file_path):
    with open(file_path, "rb") as f:
        loaded_personas = pickle.load(f)

    loaded_personas.sort(key=lambda x: x.identifier)
    
    print("Name\t\tID\t\tEmail\t\t\tAge")
    for p in loaded_personas:
        print(f"{p.name}\t\t{p.identifier}\t{p.email}\t\t{p.age}")

@dataclass
class Person:
    name: str
    identifier: int
    email: str
    age: int

file = open("name_serialization.txt", "r", encoding="latin1")

data = file.readlines()
data.pop(0)

personas = []

for line in data:
    parts = line.split("\t")
    parts[3] = parts[3].replace("\n", "")

    person = Person(parts[0], parts[1], parts[2], int(parts[3]))
    personas.append(person)

with open("person_data.pickle", "wb") as f:
    pickle.dump(personas, f)

process_data("person_data.pickle")
