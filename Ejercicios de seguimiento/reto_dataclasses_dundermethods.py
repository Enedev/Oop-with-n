from dataclasses import dataclass 

@dataclass
class Banco():
    clientesTotales = []

    @classmethod
    def agregarClientes(cls, clientes):
        for cliente in clientes:
            if not cls.existeCliente(cliente.id):
                cls.clientesTotales.append(cliente)
            else:
                print(f"El cliente con ID {cliente.id} ya existe en la lista de clientes totales.")

    @classmethod
    def existeCliente(cls, id):
        for cliente in cls.clientesTotales:
            if cliente.id == id:
                return True
        return False
    
    @classmethod
    def listarClientes(cls, orden_ascendente=True):
        clientes_ordenados = sorted(cls.clientesTotales, key=lambda cliente: cliente.saldo, reverse=not orden_ascendente)
        for cliente in clientes_ordenados:
            print(cliente)

@dataclass
class Cliente():
    id: int
    name: str
    saldo: float = 0.0
    clientes = []

    def __post_init__(self):
        Cliente.clientes.append(self)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.name}, Saldo: {self.saldo}"
    
    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def transferir(self, destinatario, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            destinatario.saldo += cantidad
        else:
            print("Saldo insuficiente")


    
cliente1 = Cliente(12,"ugu")
cliente2 = Cliente(14,"ugunt")
cliente3 = Cliente(32,"neithan")

cliente1.depositar(1000)
cliente2.depositar(2000)
cliente3.depositar(1500)

cliente1.transferir(cliente2, 500)

todosLosClientes = Cliente.clientes

Banco.agregarClientes(todosLosClientes)

print(Banco.clientesTotales)

print("Listado de clientes (orden ascendente por saldo):")
Banco.listarClientes()

print("\nListado de clientes (orden descendente por saldo):")
Banco.listarClientes(orden_ascendente=False)






    





    
