def f():
  print("función fuera del try...")
try:
  def g():
    print("función dentro del try...")
  #error de sintaxis o lógico?
  a = ["Ay","muchachos..."]
  print(a[0])
  print(a[1])
  print(a[2])
except:
  print("Grave...")
  f()
  g()