from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    libros_prestados: int = 0
    libros_reservados: int = 0
    libros_no_regresados: int = 0
    libros_botados: int = 0
    multas: float = 0.0

@dataclass
class Libro:
    titulo: str
    autor: str
    isbn: str
    reserva: bool = True

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente.")

    def eliminar_libro(self, libro: Libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado correctamente.")
        else:
            print("El libro no existe en la biblioteca.")

    def buscar_libro_por_titulo(self, titulo: str):
        libros_encontrados = []
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libro_por_autor(self, autor: str):
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def mostrar_informacion_libro(self, libro: Libro):
        print("Información del libro:")
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"ISBN: {libro.isbn}")
        print(f"Disponible para reserva: {'Sí' if libro.reserva else 'No'}")

if __name__ == "__main__":
    # Crear usuarios
    estudiante = Usuario("Juan", libros_prestados=2)
    administrativo = Usuario("María", libros_prestados=1, libros_reservados=1)

    # Crear biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "9788437604947")
    libro2 = Libro("1984", "George Orwell", "9780451524935")
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9788420412146")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Buscar libros por título
    libros_encontrados = biblioteca.buscar_libro_por_titulo("1984")
    for libro in libros_encontrados:
        biblioteca.mostrar_informacion_libro(libro)

    # Buscar libros por autor
    libros_encontrados = biblioteca.buscar_libro_por_autor("Gabriel García Márquez")
    for libro in libros_encontrados:
        biblioteca.mostrar_informacion_libro(libro)
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    tipo: str  # "estudiante" o "administrativo"
    libros_prestados: int = 0
    libros_reservados: int = 0
    libros_no_regresados: int = 0
    libros_botados: int = 0
    multas: float = 0.0

@dataclass
class Libro:
    titulo: str
    autor: str
    isbn: str
    reserva: bool = True

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro: Libro, usuario: Usuario, prestado: bool = True):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente.")

        if prestado:
            if usuario.tipo == "estudiante":
                usuario.libros_prestados += 1
            elif usuario.tipo == "administrativo":
                usuario.libros_prestados += 1
            else:
                print("Tipo de usuario no válido.")
        else:
            usuario.libros_reservados += 1

    def eliminar_libro(self, libro: Libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado correctamente.")
        else:
            print("El libro no existe en la biblioteca.")

    def buscar_libro_por_titulo(self, titulo: str):
        libros_encontrados = []
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libro_por_autor(self, autor: str):
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def mostrar_informacion_libro(self, libro: Libro):
        print("Información del libro:")
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"ISBN: {libro.isbn}")
        print(f"Disponible para reserva: {'Sí' if libro.reserva else 'No'}")

if __name__ == "__main__":
    # Crear usuarios
    estudiante = Usuario("Juan", "estudiante", libros_prestados=2)
    administrativo = Usuario("María", "administrativo", libros_prestados=1, libros_reservados=1)

    # Crear biblioteca
    biblioteca = Biblioteca()
    print("------------------")

    # Agregar libros a la biblioteca
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "9788437604947")
    libro2 = Libro("1984", "George Orwell", "9780451524935")
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9788420412146")

    biblioteca.agregar_libro(libro1, estudiante, prestado=True)
    biblioteca.agregar_libro(libro3, administrativo, prestado=False)
    print(estudiante.libros_prestados)

     # Eliminar libro de la biblioteca
    biblioteca.eliminar_libro(libro2)

    # Modificar información de un libro en la biblioteca
    libro1.titulo = "Cien años de soledad (Edición Especial)"
    libro1.autor = "Gabriel García Márquez (Edición Especial)"
    libro1.isbn = "9788437604947 (Edición Especial)"
    libro1.reserva = False

    # Mostrar información actualizada del libro
    #biblioteca.mostrar_informacion_libro(libro1)

    # Buscar libros por título
    print("------------------")

    libros_encontrados = biblioteca.buscar_libro_por_titulo("1984")
    for libro in libros_encontrados:
        biblioteca.mostrar_informacion_libro(libro)

    # Buscar libros por autor
    print("------------------")

    libros_encontrados = biblioteca.buscar_libro_por_autor("Gabriel García Márquez (Edición Especial)")
    for libro in libros_encontrados:
        biblioteca.mostrar_informacion_libro(libro)


