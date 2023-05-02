class ExcAPOO(Exception):
  pass

try:
  if(c1):
    raise ExcAPOO("Grave...")
except ExcAPOO as e:
  print("Se detectó una excepción de tipo ExcAPOO")

except:
  print("Error!!")