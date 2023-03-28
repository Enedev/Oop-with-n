from dataclasses import dataclass

@dataclass
class Person:
    _name: str
    _id: int
    _age : int
    _distance_traveled : int

    def __repr__(self):
        return '{' + self._name + ', ' + str(self._id) + ', ' + str(self._age) + ', ' + str(self._distance_traveled) + '}'
    
    #def __repr__(self):
        #return self._name
    
    def walk(self, distance: str | int) -> str:
        distance: int
        self._distance_traveled += distance
        return self._distance_traveled
    
    def __lt__(self, other): #parte solución f1()
        return len(self._name)<len(other._name)

