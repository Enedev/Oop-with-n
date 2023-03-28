from typing import * #Importación de la librería

#Tipos contenedores
int_list:List[int] = [1,2,3,4]
str_set:Set[str] = {"a","b","c"}
str_int_dict:Dict[str,int] = {"a":1, "b":2}
print(int_list)
print(str_set)
print(str_int_dict)

def traverse_sequence(sequence:Sequence) -> None: #retorno vacía -> None
  for element in sequence:
    print(element)
    
traverse_sequence([2,3,4])