class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        return resultados

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("El Quijote", "Miguel de Cervantes", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "0987654321")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()

resultados = biblioteca.buscar_libro_por_titulo("El Quijote")
if resultados:
    print("\nResultados de la búsqueda:")
    for libro in resultados:
        print(libro)
else:
    print("\nNo se encontraron libros con ese título.")
