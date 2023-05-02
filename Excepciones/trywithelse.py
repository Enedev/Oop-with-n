def f(a):
  if(a<4):
    b = a/(a-3)
  print("b",b)

try:
  f(2)
  f(5)
except ZeroDivisionError:
  print("Divisón por cero!")
except NameError:
  print("Error de nombre!")
else:
  print("Se ejecutó bien...")