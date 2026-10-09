# Ejercicio 11 - Estudiante y sus materias

class Estudiante:

  def __init__(self, nombre):
    self.nombre = nombre
    self.materias = {}  # Diccionario para guardar materia: nota

  def registrar_nota(self, materia, nota):
    self.materias[materia] = nota

  def calcular_promedio(self):
    if not self.materias:
      return 0
    return sum(self.materias.values()) / len(self.materias)

  def esta_aprobado(self, nota_minima=60):
    # Evaluamos si el promedio llega o supera la nota mínima de aprobación
    return self.calcular_promedio() >= nota_minima

  def mostrar_boletin(self):
    print(f"\n🎓 Boletín Académico de: {self.nombre}")
    for mat, nota in self.materias.items():
      print(f" - {mat}: {nota}")
    prom = self.calcular_promedio()
    estado = "APROBADO 🎉" if self.esta_aprobado() else "REPROBADO ❌"
    print(f"Promedio General: {prom:.1f} | Condición: {estado}")


estu = Estudiante("Mateo Duarte")
estu.registrar_nota("Matemáticas", 75)
estu.registrar_nota("Programación", 85)
estu.registrar_nota("Física", 70)
estu.mostrar_boletin()