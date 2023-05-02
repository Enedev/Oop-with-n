class ErrorTerminos(Exception):
    pass

class ZeroDivisionError(Exception):
    pass
class ErrorNum(Exception):
    pass


class Calculadora:
    
    def __init__(self):
        self.operadores=["+","-","*","/"]
    
    def calcular(self):
        op= input("Ingrese la operación que desea realizar: ")
        expresion= op.split()
        print(op)

        try:
            if len(expresion)!= 3:
                raise ErrorTerminos("La expresión no tiene la cantidad correcta de términos.")
            if not expresion[0].isdigit() or not expresion[2].isdigit():
                raise ErrorNum("La expresión contiene un número no válido.")
            if expresion[1] not in self.operadores:
                raise ErrorTerminos("La expresión contiene un operador no válido.")
            
            opdL= float(expresion[0])
            opdR= float(expresion[2])
            operator= expresion[1]

            if operator == "+":
                result= opdL + opdR
            elif operator == "-":
                result= opdL - opdR
            elif operator == "*":
                result= opdL * opdR
            elif operator == "/":
                if opdR== 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                else:
                    result= opdL / opdR
            
            print("El resultado de la operación es:", result)
        
        except ErrorTerminos as et:
            print("Error de terminos:", et)
        except ErrorNum as en:
            print("Error numérico:", en)
        except ZeroDivisionError as dc:
            print("Error de división:", dc)
        except:
            print("Error desconocido.")

x= Calculadora()
x.calcular()
