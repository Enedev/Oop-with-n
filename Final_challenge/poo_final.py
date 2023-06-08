class Car:
    owner = ''
    column = 0
    row = 0
    def __init__(self, plate, km, position):
        self.plate = plate
        self.km = km
        self.position = position

class Owner:
    def __init__(self, name, age, car_plate) -> None:
        self.name = name
        self.age = age
        self.car_plate = car_plate

file = open('final_challenge.txt', 'r', encoding='utf-8').read()

lines_arr = file.splitlines()

#Fill garage with size found
def fill_garage(size):
    #Filling the nxn matrix 
    for i in range(size):
        arr = []
        for j in range(size):
            arr.append('-')
        garage.append(arr)

#Where we'll store our cars
garage = []

#Find size of the garage
for i in lines_arr:
    try: 
        int(i)
        #Finding size
        print(f'Size found {i}')
        fill_garage(int(i))
        lines_arr.remove(i)
    except:
        continue

def remove_unwanted_characters(arr):
    """ print(arr, 'hi') """
    row = arr[2]
    column = arr[3]

    symbols = ',)('

    for i in symbols:
        row = row.replace(i, '')
        column = column.replace(i, '')
    
    return row, column


def isOwner(data):
    #Check for owner
    for i in data:
        if (i == '('):
            #It's a car
            return False
    #It's an owner
    split_data = data.split()
    return Owner(split_data[0], split_data[1], split_data[2])

def findCar(data, owner):
    for car in data:
        car_info = car.split()
        if car_info[0] != owner.name and car_info[0] == owner.car_plate:
            row, column = remove_unwanted_characters(car_info)
            new_car = Car(car_info[0], car_info[1], car_info[2])
            new_car.row = int(row)
            new_car.column = int(column)
            return new_car
        else:
            continue
    
    return False

def findOwner(data, car):
    for owner in data:
            if owner[0] != car.plate and owner[2] == car.plate:
                new_owner = Owner(owner[0], owner[1], owner[2])
                return new_owner
            else:
                continue

def add_car_to_garage(car, owner = None):
    
    if owner == None:
        garage[car.row][car.column] = f'{car.plate}(None)'
    else:
        garage[car.row][car.column] = f'{car.plate}({owner.name})'
        

#For loop controller, we want i to increase 2 each time

def create_garage(all_data):
    for aux in all_data:

        owner_data = isOwner(aux)
        #Finding car for owner
        if owner_data != False:
            car_data = findCar(all_data, owner_data)

            if car_data != False:
                car_data.owner = owner_data
                add_car_to_garage(car_data, owner_data)
                #Remove owner from the array, this can be dangerous but who cares! I ain't making no copy of the array
                if aux in all_data:
                    lines_arr.remove(aux)
                    #Continue the iteration
                    continue
            else:
                #If car wasn't found, we completely ignore it
                continue
        #In case the line is a car, we must find it an owner
        else:
            car_data = aux.split()
            row, column = remove_unwanted_characters(car_data)
            car = Car(car_data[0], car_data[1], car_data[2])
            car.row = int(row)
            car.column = int(column)
            add_car_to_garage(car)

create_garage(lines_arr)
print(garage)