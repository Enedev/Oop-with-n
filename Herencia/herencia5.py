class A:
  def __init__(self):
    self.a = 5
class B(A):
  def __init__(self):
    super().__init__()
    pass

b = B()
print(b.a) #qué imprime? - ??