class A:
  def __init__(self):
    print("Constructor a")
    self.message = "Soy A"
    print(self.message)
  def print_message(self):
    print(self.message)
class B:
  def __init__(self):
    print("Constructor b")
    self.value = "Soy B"

    print(self.message)
  def print_value(self):
    print(self.message)
class C(A,B):
  def __init__(self):
    super().__init__()

c = C() #qué pasa?
#c.print_value()
#b= B()
#b.print_value()

class A:
  def __init__(self):
    self.message = "Soy A"
    self.print_message()
  def print_message(self):
    print(self.message)
class B:
  def __init__(self):
    self.value = "Soy B"
    self.message = "message B"
    self.print_value()
  def print_value(self):
    print(self.value)
class C(B,A):
  def __init__(self):
    A.__init__(self)
    B.__init__(self)

c = C() #qué pasa?
c.print_message() #qué pasa?
c.print_value() #qué pasa?
print(c.message) #qué pasa?
print(c.value) #qué pasa?