# Ejercicio 4 - Libro de una biblioteca

class Libro:

  def __init__(self, titulo, autor, disponible=True):
    self.titulo = titulo
    self.autor = autor
    self.disponible = disponible  # Arranca True (disponible) o False (prestado)

  def __str__(self):
    estado = "Disponible" if self.disponible else "Prestado"
    return f"Libro: '{self.titulo}' de {self.autor} - Estado: [{estado}]"


libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", True)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)

print(libro1)
print(libro2)