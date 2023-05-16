class OperacionInvalidaError(Exception):
    pass

class OperadorInvalidoError(Exception):
    pass

class Calculadora:
    def __init__(self):
        self.operadores_validos = ['+', '-', '*', '/']

    def evaluar_expresion(self, expresion):
        try:
            operandos = expresion.split()
            if len(operandos) != 3:
                raise OperacionInvalidaError("Expresión inválida: {}".format(expresion))

            operando1 = float(operandos[0])
            operador = operandos[1]
            operando2 = float(operandos[2])

            if operador not in self.operadores_validos:
                raise OperadorInvalidoError("Operador inválido: {}".format(operador))

            if operador == '+':
                resultado = operando1 + operando2
            elif operador == '-':
                resultado = operando1 - operando2
            elif operador == '*':
                resultado = operando1 * operando2
            elif operador == '/':
                if operando2 == 0:
                    raise OperacionInvalidaError("División por cero")
                resultado = operando1 / operando2

            return resultado

        except ValueError:
            raise OperacionInvalidaError("Expresión inválida: {}".format(expresion))

    def ejecutar_calculadora(self):
        while True:
            expresion = input("Ingrese una expresión o escriba 'terminar' para salir: ")

            if expresion == 'terminar':
                break

            try:
                resultado = self.evaluar_expresion(expresion)
                print("Resultado: {}".format(resultado))
            except (OperacionInvalidaError, OperadorInvalidoError) as e:
                print("Error: {}".format(str(e)))
                print("Ingrese una nueva expresión.")

calculadora = Calculadora()
calculadora.ejecutar_calculadora()
