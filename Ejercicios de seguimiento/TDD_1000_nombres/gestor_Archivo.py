import random

class FileManager:
    def generate_file(self):
        with open("1000_names.txt", "w") as f:
            for name, age in zip(self.generate_names(), self.generate_ages()):
                data = f"{name},{age}\n"
                f.write(data)

    def read_file(self):
        pass

    def write_file(self):
        pass

    def generate_names(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        names = []
        for _ in range(1000):
            length = random.randint(1, 10)
            name = ""
            for _ in range(length):
                name += random.choice(letters)
            names.append(name)
        return names

    def generate_ages(self):
        ages = []
        for _ in range(1000):
            age = random.randint(1, 99)
            ages.append(age)
        return ages

    def create_people(self):
        pass

file_manager = FileManager()
file_manager.generate_file()
print("File generated successfully.")
file_manager.generate_names()
