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
