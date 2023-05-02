from dataclasses import dataclass
PI = 3.1415

@dataclass
class Figura:
  nombre:str
  color:str
  def dibujar(self) -> None:
    print("Dibujando una figura...")

@dataclass
class Figura2D(Figura):
  def dibujar(self) -> None:
    super().dibujar()
    print("Dibujando una figura 2D...")
  
  def calcular_area(self):
    print("Calculando área figura 2d")
  
  def calcular_perimetro(self):
    print("Calculando área figura 2d")

  def cambiar_tamanho(self):
    print("Cambiando tamaño...")

@dataclass
class Circulo(Figura2D):
  radio:float
  def cambiar_tamanho(self):
    print("Cambiando tamaño de círculo...")
  def calcular_area(self):
    return PI*(self.radio**2)
  def calcular_perimetro(self):
    return PI*(self.radio * 2)
  
@dataclass
class Cuadrado(Figura2D):
  lado:float
  def cambiar_tamanho(self):
    print("Cambiando tamaño de cuadrado...")
  def calcular_area(self):
    return self.lado ** 2
  def calcular_perimetro(self):
    return self.lado * 4
  
@dataclass
class Triangulo(Figura2D):
  base:float
  altura:float
  def cambiar_tamanho(self):
    print("Cambiando tamaño de triángulo...")
  def calcular_area(self):
    return (self.base * self.altura) / 2
  def calcular_perimetro(self):
    return self.base * 3
  

@dataclass
class Figura3D(Figura):
    def dibujar(self) -> None:
        super().dibujar()
        print("Dibujando una figura 3D...")
    
    def calcular_volumen(self):
        print("Calculando volumen figura 3D...")
    
    def cambiar_tamanho(self):
        print("Cambiando tamaño...")

@dataclass
class Esfera(Figura3D):
    radio:float
    def cambiar_tamanho(self):
        print("Cambiando tamaño de esfera...")
    def calcular_volumen(self):
        return (4/3) * PI * (self.radio ** 3)

@dataclass
class Cubo(Figura3D):
    lado:float
    def cambiar_tamanho(self):
        print("Cambiando tamaño de cubo...")
    def calcular_volumen(self):
        return self.lado ** 3

@dataclass
class Piramide(Figura3D):
    base:float
    altura:float
    def cambiar_tamanho(self):
        print("Cambiando tamaño de piramide...")
    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3


#FIGURAS 2D

#cuadrado
print("---------")
c1 = Cuadrado("c1","b",5)
c1.dibujar()
c1.cambiar_tamanho()
print("área", c1.calcular_area())
print("perímetro", c1.calcular_perimetro())

#triángulo
print("---------")
t1 = Triangulo("t1","b",5,6)
t1.dibujar()
t1.cambiar_tamanho()
print("área", t1.calcular_area())
print("perímetro", t1.calcular_perimetro())

#círculo
print("---------")
ci1 = Circulo("c1","b",9)
ci1.dibujar()
ci1.cambiar_tamanho()
print("área", ci1.calcular_area())
print("perímetro", ci1.calcular_perimetro())

figuras = [c1,t1,ci1]
for i in figuras:
  print(i.calcular_area())
  print(i.calcular_perimetro())
  print("----------")

#FIGURAS 3D


#esfera
print("---------")
e1 = Esfera("e1","b",9)
e1.dibujar()
e1.cambiar_tamanho()
print("volumen", e1.calcular_volumen())

#cubo
print("---------")
c1 = Cubo("c1","b",5)
c1.dibujar()
c1.cambiar_tamanho()
print("volumen", c1.calcular_volumen())

#piramide
print("---------")
p1 = Piramide("p1","b",5,6)
p1.dibujar()
p1.cambiar_tamanho()
print("volumen", p1.calcular_volumen())

figuras = [e1,c1,p1]
for i in figuras:
    print(i.calcular_volumen())
    print("----------")
