class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  
  def get_price(self):
    return self.price

class OrderItem:
  def __init__(self, order_data):
    self.product = Product(order_data[0], order_data[1])
    self.count = order_data[2]
  
  def get_order_total(self):
    return self.count * self.product.get_price()

class OrderList:
  def __init__(self, order_data):
    self.items = []
    self.create_orders(order_data) #Llenar self.items

  def create_orders(self, order_data):
    for order_data in order_data.values():
      order = OrderItem(order_data)
      self.items.append(order) #agregando cada orden creada

  #calculando sumatoria total
  def get_order_list_total(self):
    total = 0
    for order in self.items:
      order_price = order.get_order_total()
      total += order_price
    return total

def main():

  datos = {"op1":["p1",100,3],"op2": ["p2",200,2],
           "op3": ["p3",300,5]}
  #orden final
  final_order = OrderList(datos)
  total = final_order.get_order_list_total()
  print(total)


if __name__ == '__main__':
    # Se ejecuta cuando el módulo no es importado
    main()