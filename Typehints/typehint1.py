from typing import Union #Type union

#si pueden ser ambos
def sum(a:Union[int,float],b:Union[float, int]) -> Union[float,int]:
  return a+b

print(sum(5,6.5))

def sumx(a:int|float,b:float|int) -> float|int:
  return a+b

print(sumx(5,6.5))