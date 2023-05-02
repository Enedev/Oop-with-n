def f():
  try:
    print("Estoy en el try...")
    a = [10,5,3]
    idx = int(input())
    print(a[idx])
  except:
    print("Entré al except... ")
    f()

f()